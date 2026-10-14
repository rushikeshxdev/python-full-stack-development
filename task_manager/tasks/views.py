from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework.permissions import AllowAny
from .permissions import IsOwnerOrReadOnly, TaskRolePermission
from rest_framework import permissions
from drf_spectacular.utils import extend_schema

from .models import Task, Project, Tag
from .serializers import (
    TaskSerializer,
    RegisterSerializer,
    ProjectSerializer,
    TagSerializer,
    TaskMetricsSerializer,
)
from .services import get_task_metrics


class OwnerCreateMixin:
    """Reusable mixin that automatically sets the logged-in user as the resource owner."""
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@extend_schema(tags=['Tasks'])
class TaskListCreateView(OwnerCreateMixin, generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, TaskRolePermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority', 'status']

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.select_related('owner', 'assigned_to', 'project').prefetch_related('tags')
        return Task.objects.none()


@extend_schema(tags=['Tasks'])
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, TaskRolePermission]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.select_related('owner', 'assigned_to', 'project').prefetch_related('tags')
        return Task.objects.none()


@extend_schema(
    tags=['Analytics & Metrics'],
    summary='Retrieve aggregated task statistics',
    responses={200: TaskMetricsSerializer}
)
class TaskMetricsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        metrics = get_task_metrics()
        return Response(metrics, status=status.HTTP_200_OK)


@extend_schema(tags=['Authentication'], summary='Register a new user account')
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=['Projects'])
class ProjectListCreateView(OwnerCreateMixin, generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Project.objects.select_related('owner')
        return Project.objects.none()


@extend_schema(tags=['Projects'])
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Project.objects.select_related('owner')
        return Project.objects.none()


@extend_schema(tags=['Tags'])
class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None


@extend_schema(tags=['Tags'])
class TagDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]