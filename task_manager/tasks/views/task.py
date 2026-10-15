from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import extend_schema

from ..models import Task, Tag
from ..serializers import TaskSerializer, TagSerializer
from ..permissions import TaskRolePermission
from .base import OwnerCreateMixin


class BaseTaskView:
    """Shared base configuration for Task endpoints to prevent duplicate code."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, TaskRolePermission]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.select_related('owner', 'assigned_to', 'project').prefetch_related('tags')
        return Task.objects.none()


@extend_schema(tags=['Tasks'])
class TaskListCreateView(OwnerCreateMixin, BaseTaskView, generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority', 'status']


@extend_schema(tags=['Tasks'])
class TaskDetailView(BaseTaskView, generics.RetrieveUpdateDestroyAPIView):
    pass


class BaseTagView:
    """Shared base configuration for Tag endpoints."""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]


@extend_schema(tags=['Tags'])
class TagListCreateView(BaseTagView, generics.ListCreateAPIView):
    pagination_class = None


@extend_schema(tags=['Tags'])
class TagDetailView(BaseTagView, generics.RetrieveUpdateDestroyAPIView):
    pass

