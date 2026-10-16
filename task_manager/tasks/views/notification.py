from rest_framework import generics, permissions, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from ..models import Notification
from ..serializers import NotificationSerializer


@extend_schema(tags=['Notifications'])
class NotificationListView(generics.ListAPIView):
    """List notifications for the currently authenticated user."""
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Notification.objects.filter(recipient=user).select_related('recipient', 'actor', 'task')
        unread_only = self.request.query_params.get('unread')
        if unread_only and unread_only.lower() in ('true', '1'):
            queryset = queryset.filter(is_read=False)
        return queryset


@extend_schema(tags=['Notifications'])
class NotificationMarkReadView(generics.UpdateAPIView):
    """Mark a notification as read."""
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['patch']

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user)

    def patch(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.is_read = True
        notification.save(update_fields=['is_read'])
        serializer = self.get_serializer(notification)
        return Response(serializer.data, status=status.HTTP_200_OK)
