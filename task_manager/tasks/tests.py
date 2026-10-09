from django.test import TestCase
from django.contrib.auth.models import User, Group
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task, Project, Tag
from .constants import TaskStatus, TaskPriority
from .services import get_task_metrics


class TaskAPITestCase(TestCase):
    def setUp(self):
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

        # Trying to edit self.task1 which is owned by self.user
        response = self.client.patch(f'/api/v1/tasks/{self.task1.id}/', {"title": "Hacked Title"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_admin_can_edit_other_user_task(self):
        admin_user = User.objects.create_user(username="admin_user", password="password123")
        admin_group = Group.objects.create(name="Admin")
        admin_user.groups.add(admin_group)

        self.client.force_authenticate(user=admin_user)
        # Admin can edit self.task1 even though they are not the owner
        response = self.client.patch(f'/api/v1/tasks/{self.task1.id}/', {"title": "Admin Updated Title"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, "Admin Updated Title")
