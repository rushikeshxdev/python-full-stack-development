from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Task
from .serializers import TaskSerializer
from .services import get_task_metrics


class TaskListCreateView(generics.ListCreateAPIView):
    """
    Generic View for Task Collection:
    - GET  /api/v1/tasks/     -> List tasks with filtering, search, and ordering
    - POST /api/v1/tasks/     -> Create a new task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Exact match filters: ?status=TODO&priority=HIGH
    filterset_fields = ['status', 'priority']

    # Search keyword filter: ?search=deploy
    search_fields = ['title', 'description']

    # Ordering fields: ?ordering=-created_at
    ordering_fields = ['created_at', 'due_date', 'priority', 'status']


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic View for Single Task Operations:
    - GET    /api/v1/tasks/<id>/  -> Retrieve task details
    - PUT    /api/v1/tasks/<id>/  -> Full update
    - PATCH  /api/v1/tasks/<id>/  -> Partial update
    - DELETE /api/v1/tasks/<id>/  -> Delete task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskMetricsView(APIView):
    """
    Basic APIView consuming reusable service layer functions.
    - GET /api/v1/tasks/metrics/ -> Real-time task statistics
    """
    def get(self, request, *args, **kwargs):
        metrics = get_task_metrics()
        return Response(metrics, status=status.HTTP_200_OK)
