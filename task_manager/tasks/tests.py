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
