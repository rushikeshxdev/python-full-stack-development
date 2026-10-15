from datetime import date, timedelta
import pytest
from django.contrib.auth.models import User, Group

from tasks.constants import TaskStatus, TaskPriority
from tasks.serializers import (
    TaskSerializer,
    RegisterSerializer,
    ProjectSerializer,
    TagSerializer,
)


@pytest.mark.django_db
class TestTaskSerializer:
    """Unit tests for TaskSerializer validation rules."""

    def test_valid_task_data(self):
        """Positive test: Valid data passes validation."""
        tomorrow = date.today() + timedelta(days=1)
        data = {
            'title': 'Write Comprehensive Tests',
            'description': 'Testing models, serializers, and views',
            'status': TaskStatus.TODO,
            'priority': TaskPriority.HIGH,
            'due_date': tomorrow.isoformat(),
        }
        serializer = TaskSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        assert serializer.validated_data['title'] == 'Write Comprehensive Tests'

    def test_title_too_short_fails_validation(self):
        """Negative test: Title with fewer than 3 characters is rejected."""
        data = {
            'title': 'Hi',
            'status': TaskStatus.TODO,
        }
        serializer = TaskSerializer(data=data)
        assert not serializer.is_valid()
        assert 'title' in serializer.errors
        assert "at least 3 characters" in str(serializer.errors['title'][0])

    def test_title_only_digits_fails_validation(self):
        """Negative test: Title containing only digits is rejected."""
        data = {
            'title': '12345',
            'status': TaskStatus.TODO,
        }
        serializer = TaskSerializer(data=data)
        assert not serializer.is_valid()
        assert 'title' in serializer.errors
        assert "cannot contain only numbers" in str(serializer.errors['title'][0])

    def test_past_due_date_for_incomplete_task_fails(self):
        """Negative test: Incomplete task with past due date is rejected."""
        yesterday = date.today() - timedelta(days=1)
        data = {
            'title': 'Valid Task Title',
            'status': TaskStatus.TODO,
            'due_date': yesterday.isoformat(),
        }
        serializer = TaskSerializer(data=data)
        assert not serializer.is_valid()
        assert 'due_date' in serializer.errors
        assert "cannot be set in the past" in str(serializer.errors['due_date'][0])

    def test_past_due_date_for_completed_task_is_allowed(self):
        """Edge case: Completed task (DONE) can have a past due date."""
        yesterday = date.today() - timedelta(days=1)
        data = {
            'title': 'Archived Finished Task',
            'status': TaskStatus.DONE,
            'due_date': yesterday.isoformat(),
        }
        serializer = TaskSerializer(data=data)
        assert serializer.is_valid(), serializer.errors


@pytest.mark.django_db
class TestRegisterSerializer:
    """Unit tests for user registration serializer."""

    def test_valid_registration(self):
        """Positive test: Valid credentials pass validation."""
        data = {
            'username': 'newdeveloper',
            'email': 'dev@example.com',
            'password': 'SecurePassword123!',
        }
        serializer = RegisterSerializer(data=data)
        assert serializer.is_valid(), serializer.errors

    def test_short_password_fails_validation(self):
        """Negative test: Passwords shorter than 8 chars are rejected."""
        data = {
            'username': 'newdeveloper',
            'email': 'dev@example.com',
            'password': 'short',
        }
        serializer = RegisterSerializer(data=data)
        assert not serializer.is_valid()
        assert 'password' in serializer.errors

    def test_user_creation_auto_assigns_contributor_role(self):
        """Integration/Unit test: Saving creates user with hashed password & Contributor role."""
        data = {
            'username': 'role_test_user',
            'email': 'role_test@example.com',
            'password': 'SecurePassword123!',
        }
        serializer = RegisterSerializer(data=data)
        assert serializer.is_valid()
        user = serializer.save()

        assert user.pk is not None
        assert user.check_password('SecurePassword123!')  # Password was hashed
        assert user.groups.filter(name='Contributor').exists()  # Auto-assigned role
