from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that provides full CRUD operations on tasks:
    - List tasks (with pagination, filtering, searching, and ordering)
    - Create a new task
    - Retrieve a specific task by ID
    - Update a task (PUT/PATCH)
    - Delete a task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Filter tasks by exact match on status and priority (e.g., ?status=TODO&priority=HIGH)
    filterset_fields = ['status', 'priority']

    # Search tasks by keyword in title or description (e.g., ?search=deploy)
    search_fields = ['title', 'description']

    # Order tasks by field (e.g., ?ordering=-created_at or ?ordering=due_date)
    ordering_fields = ['created_at', 'due_date', 'priority', 'status']
