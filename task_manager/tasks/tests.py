from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from .constants import TaskStatus, TaskPriority
from .services import get_task_metrics


class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task1 = Task.objects.create(
            title="Initial Test Task",
            description="Testing generic views",
            status=TaskStatus.TODO,
            priority=TaskPriority.HIGH
        )

    def test_list_tasks_v1(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_create_task_v1(self):
        payload = {
            "title": "New Generic View Task",
            "description": "Created via v1 API",
            "status": TaskStatus.IN_PROGRESS,
            "priority": TaskPriority.MEDIUM
        }
        response = self.client.post('/api/v1/tasks/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Generic View Task")

    def test_task_detail_patch_v1(self):
        payload = {"status": TaskStatus.DONE}
        response = self.client.patch(f'/api/v1/tasks/{self.task1.id}/', payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.status, TaskStatus.DONE)

    def test_task_metrics_service_and_endpoint(self):
        metrics = get_task_metrics()
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
