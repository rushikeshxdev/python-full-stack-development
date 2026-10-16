from rest_framework import serializers
from ..models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    recipient = serializers.ReadOnlyField(source='recipient.username')
    actor = serializers.ReadOnlyField(source='actor.username')
    task_title = serializers.ReadOnlyField(source='task.title')

    class Meta:
        model = Notification
        fields = [
            'id',
            'recipient',
            'actor',
            'task',
            'task_title',
            'verb',
            'is_read',
            'created_at',
        ]
        read_only_fields = ['id', 'recipient', 'actor', 'task', 'task_title', 'verb', 'created_at']
