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

from .models import Task, Project, Tag
from .serializers import TaskSerializer, RegisterSerializer, ProjectSerializer, TagSerializer
from .services import get_task_metrics


class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, TaskRolePermission]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'priority']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'due_date', 'priority', 'status']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            queryset = Task.objects.select_related('owner', 'assigned_to', 'project').prefetch_related('tags')
            if user.is_staff or user.groups.filter(name__in=['Admin', 'Viewer']).exists():
                return queryset
            return queryset.filter(Q(owner=user) | Q(assigned_to=user))
        return Task.objects.none()

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, TaskRolePermission]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.select_related('owner', 'assigned_to', 'project').prefetch_related('tags')
        return Task.objects.none()

class TaskMetricsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        metrics = get_task_metrics(user=request.user)
        return Response(metrics, status=status.HTTP_200_OK)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ProjectListCreateView(generics.ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff:
                return Project.objects.all()
            return Project.objects.filter(owner=user)
        return Project.objects.none()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None