import pytest
from unittest.mock import patch
from django.contrib.auth.models import User
from tasks.models import Task, Notification
from tasks.tasks import send_task_notification_async


@pytest.mark.django_db
class TestNotificationModel:
    def test_notification_creation_and_defaults(self, admin_user, contributor_user, sample_project):
        task = Task.objects.create(
            title="Notification Test Task",
            description="Testing notification creation",
            owner=admin_user,
            assigned_to=contributor_user,
            project=sample_project
        )
        notif = Notification.objects.create(
            recipient=contributor_user,
            actor=admin_user,
            task=task,
            verb="assigned you to task"
        )
        assert notif.id is not None
        assert notif.is_read is False
        assert notif.recipient == contributor_user
        assert notif.actor == admin_user
        assert notif.task == task
        assert str(notif) == f"To {contributor_user.username}: {admin_user.username} assigned you to task"


@pytest.mark.django_db
class TestNotificationAPIEndpoints:
    def test_unauthenticated_cannot_access_notifications(self, api_client):
        response = api_client.get('/api/v1/notifications/')
        assert response.status_code == 401

    def test_recipient_only_sees_own_notifications(self, auth_client_factory, admin_user, contributor_user, viewer_user):
        Notification.objects.create(
            recipient=contributor_user,
            actor=admin_user,
            verb="assigned task A"
        )
        Notification.objects.create(
            recipient=viewer_user,
            actor=admin_user,
            verb="assigned task B"
        )

        contrib_client = auth_client_factory(contributor_user)
        res = contrib_client.get('/api/v1/notifications/')
        assert res.status_code == 200
        # Check that contributor only sees 1 notification (theirs)
        results = res.data.get('results', res.data)
        assert len(results) == 1
        assert results[0]['verb'] == "assigned task A"

    def test_mark_notification_as_read(self, auth_client_factory, admin_user, contributor_user):
        notif = Notification.objects.create(
            recipient=contributor_user,
            actor=admin_user,
            verb="read me please"
        )
        assert notif.is_read is False

        contrib_client = auth_client_factory(contributor_user)
        res = contrib_client.patch(f'/api/v1/notifications/{notif.id}/read/')
        assert res.status_code == 200
        assert res.data['is_read'] is True

        notif.refresh_from_db()
        assert notif.is_read is True

    def test_user_cannot_mark_another_users_notification(self, auth_client_factory, admin_user, contributor_user, viewer_user):
        notif = Notification.objects.create(
            recipient=contributor_user,
            actor=admin_user,
            verb="private notification"
        )

        viewer_client = auth_client_factory(viewer_user)
        res = viewer_client.patch(f'/api/v1/notifications/{notif.id}/read/')
        assert res.status_code == 404

        notif.refresh_from_db()
        assert notif.is_read is False


@pytest.mark.django_db
class TestCeleryNotificationTask:
    def test_send_task_notification_async_success(self, admin_user, contributor_user, sample_project):
        task = Task.objects.create(
            title="Celery Background Task",
            description="Testing worker dispatch",
            owner=admin_user,
            assigned_to=contributor_user,
            project=sample_project
        )

        result = send_task_notification_async(
            task_id=task.id,
            recipient_id=contributor_user.id,
            actor_id=admin_user.id,
            verb="assigned you to task: 'Celery Background Task'"
        )

        assert "SUCCESS_NOTIFICATION_ID_" in result
        notif = Notification.objects.get(task=task, recipient=contributor_user)
        assert notif.verb == "assigned you to task: 'Celery Background Task'"
        assert notif.is_read is False

    def test_celery_task_idempotency(self, admin_user, contributor_user, sample_project):
        task = Task.objects.create(
            title="Idempotency Task",
            description="Testing duplicate suppression",
            owner=admin_user,
            assigned_to=contributor_user,
            project=sample_project
        )

        first_res = send_task_notification_async(
            task_id=task.id,
            recipient_id=contributor_user.id,
            actor_id=admin_user.id,
            verb="assigned you once"
        )
        assert "SUCCESS_NOTIFICATION_ID_" in first_res

        # Call again with identical arguments
        second_res = send_task_notification_async(
            task_id=task.id,
            recipient_id=contributor_user.id,
            actor_id=admin_user.id,
            verb="assigned you once"
        )
        assert "SKIPPED_DUPLICATE_ID_" in second_res
        assert Notification.objects.filter(task=task, recipient=contributor_user).count() == 1

    def test_celery_task_dead_letter_for_missing_recipient(self, admin_user, sample_project):
        task = Task.objects.create(
            title="Dead Letter Task",
            description="Testing missing entity handling",
            owner=admin_user,
            project=sample_project
        )

        # Recipient ID 999999 does not exist
        result = send_task_notification_async(
            task_id=task.id,
            recipient_id=999999,
            actor_id=admin_user.id,
            verb="assigned to phantom"
        )

        assert "DEAD_LETTER_" in result
        assert Notification.objects.filter(task=task).count() == 0

    @patch('tasks.views.task.send_task_notification_async.delay')
    def test_create_task_triggers_celery_delay(self, mock_delay, auth_client_factory, admin_user, contributor_user):
        admin_client = auth_client_factory(admin_user)
        payload = {
            "title": "Celery Triggered Task",
            "description": "Verify view dispatches task.delay",
            "priority": "HIGH",
            "assigned_to": contributor_user.id
        }
        res = admin_client.post('/api/v1/tasks/', data=payload, format='json')
        assert res.status_code == 201

        # Check mock was called with appropriate arguments
        mock_delay.assert_called_once()
        call_args = mock_delay.call_args[0]
        assert call_args[1] == contributor_user.id  # recipient
        assert call_args[2] == admin_user.id         # actor
