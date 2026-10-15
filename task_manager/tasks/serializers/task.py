from datetime import date
from rest_framework import serializers
from ..models import Task, Tag
from ..constants import TaskStatus


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    assigned_to = serializers.ReadOnlyField(source='assigned_to.username')
    project_name = serializers.ReadOnlyField(source='project.name')
    tag_details = TagSerializer(source='tags', many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'priority',
            'due_date',
            'owner',
            'assigned_to',
            'project',
            'project_name',
            'tags',
            'tag_details',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'owner', 'assigned_to', 'project_name', 'tag_details', 'created_at', 'updated_at']

    def validate_title(self, value):
        cleaned = value.strip()
        if len(cleaned) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters long.")
        if cleaned.isdigit():
            raise serializers.ValidationError("Title cannot contain only numbers.")
        return cleaned

    def validate(self, attrs):
        status = attrs.get('status', getattr(self.instance, 'status', None))
        due_date = attrs.get('due_date', getattr(self.instance, 'due_date', None))

        # Prevent incomplete tasks from having a past due date
        if due_date and status != TaskStatus.DONE and due_date < date.today():
            raise serializers.ValidationError({
                "due_date": "Due date cannot be set in the past for an incomplete task."
            })
        return attrs
