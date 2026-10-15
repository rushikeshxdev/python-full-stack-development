from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema

from ..models import Project
from ..serializers import ProjectSerializer
from .base import OwnerCreateMixin


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
