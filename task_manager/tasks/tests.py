from django.test import TestCase
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task, Project, Tag
from .constants import TaskStatus, TaskPriority
from .services import get_task_metrics


class TaskAPITestCase(TestCase):
    def setUp(self):
        from django.core.cache import cache
        cache.clear()
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.force_authenticate(user=self.user)

        self.project = Project.objects.create(
            name="Test Project",
            description="Project description",
            owner=self.user
        )
        self.tag1 = Tag.objects.create(name="backend")
        self.tag2 = Tag.objects.create(name="database")

        self.task1 = Task.objects.create(
            title="Initial Test Task",
            description="Testing generic views",
            status=TaskStatus.TODO,
            priority=TaskPriority.HIGH,
            owner=self.user,
            project=self.project
        )
        self.task1.tags.set([self.tag1])

    def tearDown(self):
        from django.core.cache import cache
        cache.clear()

    def test_list_tasks_v1(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['project_name'], "Test Project")
        self.assertEqual(len(response.data['results'][0]['tag_details']), 1)

    def test_create_task_v1(self):
        payload = {
            "title": "New Generic View Task",
            "description": "Created via v1 API",
            "status": TaskStatus.IN_PROGRESS,
            "priority": TaskPriority.MEDIUM,
            "project": self.project.id,
            "tags": [self.tag1.id, self.tag2.id]
        }
        response = self.client.post('/api/v1/tasks/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Generic View Task")
        self.assertEqual(response.data['project'], self.project.id)
        self.assertEqual(response.data['project_name'], "Test Project")
        self.assertEqual(len(response.data['tags']), 2)

    def test_task_detail_patch_v1(self):
        payload = {"status": TaskStatus.DONE}
        response = self.client.patch(f'/api/v1/tasks/{self.task1.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.status, TaskStatus.DONE)

    def test_task_metrics_service_and_endpoint(self):
        metrics = get_task_metrics(user=self.user)
        self.assertEqual(metrics['total'], 1)
        self.assertEqual(metrics['todo'], 1)

        response = self.client.get('/api/v1/tasks/metrics/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total'], 1)

    def test_shared_and_user_scoped_task_metrics(self):
        other_user = User.objects.create_user(username='other_contrib', password='password123')
        Task.objects.create(title="Other User Task", status=TaskStatus.IN_PROGRESS, owner=other_user)

        # Shared board metrics (all tasks)
        global_metrics = get_task_metrics()
        self.assertEqual(global_metrics['total'], 2)

        # User-scoped metrics
        contrib_metrics = get_task_metrics(user=other_user)
        self.assertEqual(contrib_metrics['total'], 1)

    def test_request_logging_middleware_header(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertIn('X-Request-ID', response.headers)
        self.assertEqual(len(response.headers['X-Request-ID']), 8)

    def test_create_task_validation_error(self):
        payload = {"title": "a"}
        response = self.client.post('/api/v1/tasks/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])
        self.assertEqual(response.data['error']['code'], 'ValidationError')
        self.assertIn('title', response.data['error']['details'])
        self.assertIn('request_id', response.data)

    def test_not_found_standardized_error(self):
        response = self.client.get('/api/v1/tasks/99999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.data['success'])
        self.assertEqual(response.data['error']['code'], 'Http404')
        self.assertIn('request_id', response.data)

    def test_create_task_past_due_date_fails(self):
        from datetime import date, timedelta
        payload = {
            "title": "Task with past due date",
            "status": TaskStatus.TODO,
            "due_date": str(date.today() - timedelta(days=2))
        }
        response = self.client.post('/api/v1/tasks/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse(response.data['success'])
        self.assertIn('due_date', response.data['error']['details'])

    def test_viewer_role_cannot_create_task(self):
        viewer = User.objects.create_user(username="viewer_user", password="password123")
        viewer_group = Group.objects.create(name="Viewer")
        viewer.groups.add(viewer_group)

        self.client.force_authenticate(user=viewer)
        payload = {"title": "Viewer Forbidden Task", "status": TaskStatus.TODO}
        response = self.client.post('/api/v1/tasks/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertFalse(response.data['success'])

    def test_contributor_cannot_edit_other_user_task(self):
        other_user = User.objects.create_user(username="other_contributor", password="password123")
        self.client.force_authenticate(user=other_user)

        response = self.client.patch(f'/api/v1/tasks/{self.task1.id}/', {"title": "Updated Title"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_edit_other_user_task(self):
        admin_user = User.objects.create_user(username="admin_user", password="password123")
        admin_group = Group.objects.create(name="Admin")
        admin_user.groups.add(admin_group)

        self.client.force_authenticate(user=admin_user)
        response = self.client.patch(f'/api/v1/tasks/{self.task1.id}/', {"title": "Admin Updated Title"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, "Admin Updated Title")

    def test_contributor_cannot_delete_own_task(self):
        # Even the task owner (Contributor) cannot delete their own task
        response = self.client.delete(f'/api/v1/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Task.objects.filter(id=self.task1.id).exists())

    def test_admin_can_delete_any_task(self):
        admin_user = User.objects.create_user(username="super_admin", password="password123")
        admin_group, _ = Group.objects.get_or_create(name="Admin")
        admin_user.groups.add(admin_group)

        self.client.force_authenticate(user=admin_user)
        response = self.client.delete(f'/api/v1/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task1.id).exists())

    def test_registration_auto_assigns_contributor_group(self):
        self.client.force_authenticate(user=None)
        payload = {
            "username": "auto_contrib",
            "email": "auto@example.com",
            "password": "Password123!"
        }
        response = self.client.post('/api/v1/auth/register/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        new_user = User.objects.get(username="auto_contrib")
        self.assertTrue(new_user.groups.filter(name="Contributor").exists())

    def test_login_returns_role_in_response(self):
        self.client.force_authenticate(user=None)
        payload = {
            "username": "testuser",
            "password": "password123"
        }
        response = self.client.post('/api/v1/auth/login/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('user', response.data)
        self.assertEqual(response.data['user']['username'], "testuser")
        self.assertEqual(response.data['user']['role'], "Contributor")

    def test_cors_preflight_options_response(self):
        response = self.client.options(
            '/api/v1/tasks/',
            HTTP_ORIGIN='http://localhost:3000',
            HTTP_ACCESS_CONTROL_REQUEST_METHOD='GET'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers.get('Access-Control-Allow-Origin'), 'http://localhost:3000')

    def test_login_rate_limiting_throttle(self):
        from django.core.cache import cache
        cache.clear()
        self.client.force_authenticate(user=None)
        payload = {"username": "testuser", "password": "password123"}

        for _ in range(5):
            self.client.post('/api/v1/auth/login/', payload, format='json')

        response = self.client.post('/api/v1/auth/login/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

