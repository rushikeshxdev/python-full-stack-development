import logging
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_spectacular.utils import extend_schema

from ..models import Task, Tag
from ..serializers import TaskSerializer, TagSerializer
from ..permissions import TaskRolePermission
from ..tasks import send_task_notification_async
from .base import OwnerCreateMixin

logger = logging.getLogger(__name__)


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

    def perform_create(self, serializer):
        task = serializer.save(owner=self.request.user)
        # Asynchronously dispatch notification if assigned to another user
        if task.assigned_to and task.assigned_to != self.request.user:
            try:
                send_task_notification_async.delay(
                    task.id,
                    task.assigned_to.id,
                    self.request.user.id,
                    f"assigned you to task: '{task.title}'"
                )
            except Exception as exc:
                logger.warning(f"Failed to enqueue Celery task notification: {exc}")


@extend_schema(tags=['Tasks'])
class TaskDetailView(BaseTaskView, generics.RetrieveUpdateDestroyAPIView):
    def perform_update(self, serializer):
        prev_instance = self.get_object()
        prev_assigned_to = prev_instance.assigned_to
        prev_status = prev_instance.status

        task = serializer.save()

        # 1. New assignment notification
        if task.assigned_to and task.assigned_to != self.request.user and prev_assigned_to != task.assigned_to:
            try:
                send_task_notification_async.delay(
                    task.id,
                    task.assigned_to.id,
                    self.request.user.id,
                    f"assigned you to task: '{task.title}'"
                )
            except Exception as exc:
                logger.warning(f"Failed to enqueue Celery assignment notification: {exc}")

        # 2. Status change to DONE notification
        if prev_status != 'DONE' and task.status == 'DONE':
            if task.owner and task.owner != self.request.user:
                try:
                    send_task_notification_async.delay(
                        task.id,
                        task.owner.id,
                        self.request.user.id,
                        f"marked task '{task.title}' as completed"
                    )
                except Exception as exc:
                    logger.warning(f"Failed to enqueue Celery completion notification: {exc}")


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

