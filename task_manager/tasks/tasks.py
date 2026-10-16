import logging
from celery import shared_task
from django.contrib.auth.models import User
from .models import Task, Notification

logger = logging.getLogger(__name__)


@shared_task(bind=True, max_retries=3, default_retry_delay=2)
def send_task_notification_async(self, task_id: int, recipient_id: int, actor_id: int, verb: str):
    """
    Background worker task to create and dispatch a notification.
    Demonstrates:
    - Asynchronous execution via Redis message queue
    - Idempotency check (prevents duplicate notification records)
    - Exponential backoff retry (2s -> 4s -> 8s)
    - Dead-letter handling for missing entities
    """
    try:
        # 1. Idempotency Check
        existing = Notification.objects.filter(
            task_id=task_id,
            recipient_id=recipient_id,
            actor_id=actor_id,
            verb=verb
        ).first()

        if existing:
            logger.info(f"[CELERY IDEMPOTENCY] Notification already exists (id={existing.id}). Skipping.")
            return f"SKIPPED_DUPLICATE_ID_{existing.id}"

        # 2. Fetch related records
        recipient = User.objects.get(pk=recipient_id)
        actor = User.objects.get(pk=actor_id) if actor_id else None
        task = Task.objects.get(pk=task_id) if task_id else None

        # 3. Create Notification in PostgreSQL
        notification = Notification.objects.create(
            recipient=recipient,
            actor=actor,
            task=task,
            verb=verb,
            is_read=False
        )

        # 4. Simulate External Notification Dispatch (Email / Webhook / Slack)
        logger.info(
            f"[CELERY NOTIFICATION SUCCESS] ID={notification.id} dispatched to {recipient.username}: '{verb}'"
        )
        return f"SUCCESS_NOTIFICATION_ID_{notification.id}"

    except (User.DoesNotExist, Task.DoesNotExist) as e:
        # Permanent failure: route to dead letter logging
        logger.error(f"[CELERY DEAD-LETTER] Entity does not exist, cannot retry: {e}")
        return f"DEAD_LETTER_{e}"

    except Exception as exc:
        # Transient failure: retry with exponential backoff (2s -> 4s -> 8s)
        backoff_delay = 2 ** self.request.retries
        logger.warning(
            f"[CELERY RETRY] Task failed with {exc}. Retrying in {backoff_delay}s "
            f"(Attempt {self.request.retries + 1}/{self.max_retries})..."
        )
        raise self.retry(exc=exc, countdown=backoff_delay)
