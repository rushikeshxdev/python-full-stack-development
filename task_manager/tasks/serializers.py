from datetime import date
from rest_framework import serializers
from .models import Task, Project, Tag
from .constants import TaskStatus
from django.contrib.auth.models import User, Group
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'owner', 'created_at']
        read_only_fields = ['id', 'owner', 'created_at']


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


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        min_length=8,
        style={'input_type': 'password'}  
    )

    class Meta:
        model = User
        fields = ['id','username','email','password']
        read_only_fields = ['id']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        contributor_group, _ = Group.objects.get_or_create(name='Contributor')
        user.groups.add(contributor_group)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email

        if user.is_staff or user.groups.filter(name='Admin').exists():
            token['role'] = 'Admin'
        elif user.groups.filter(name='Viewer').exists():
            token['role'] = 'Viewer'
        else:
            token['role'] = 'Contributor'

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        role = 'Admin' if (user.is_staff or user.groups.filter(name='Admin').exists()) else (
            'Viewer' if user.groups.filter(name='Viewer').exists() else 'Contributor'
        )
        data['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': role,
        }
        return data



class TaskMetricsSerializer(serializers.Serializer):
    total = serializers.IntegerField(help_text="Total number of tasks")
    completed = serializers.IntegerField(help_text="Number of completed tasks")
    in_progress = serializers.IntegerField(help_text="Number of tasks in progress")
    todo = serializers.IntegerField(help_text="Number of todo tasks")
    high_priority = serializers.IntegerField(help_text="Number of high priority tasks")
    overdue = serializers.IntegerField(help_text="Number of overdue tasks")