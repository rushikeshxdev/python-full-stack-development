from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from ..serializers import RegisterSerializer, UserSummarySerializer


@extend_schema(tags=['Authentication'], summary='Register a new user account')
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


@extend_schema(tags=['Authentication'], summary='List active users for task assignment')
class UserListView(generics.ListAPIView):
    queryset = User.objects.filter(is_active=True).order_by('username')
    serializer_class = UserSummarySerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = None

