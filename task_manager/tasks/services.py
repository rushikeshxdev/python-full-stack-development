"""
Service layer containing reusable business logic and helper functions for tasks.
These functions can be imported and utilized across Views, Management Commands,
Celery background workers, or unit tests without coupling to HTTP request lifecycles.
"""
from datetime import date
from django.db.models import Count, Q
from .models import Task
from .constants import TaskStatus, TaskPriority


def get_task_metrics():
    """
    Computes summary metrics for tasks across the system.
    Returns a dictionary of counts.
    """
    total = Task.objects.count()
    completed = Task.objects.filter(status=TaskStatus.DONE).count()
    in_progress = Task.objects.filter(status=TaskStatus.IN_PROGRESS).count()
    todo = Task.objects.filter(status=TaskStatus.TODO).count()
    high_priority = Task.objects.filter(priority=TaskPriority.HIGH).count()

    today = date.today()
    overdue = Task.objects.filter(
        due_date__lt=today
    ).exclude(status=TaskStatus.DONE).count()

    return {
        "total": total,
        "completed": completed,
        "in_progress": in_progress,
        "todo": todo,
        "high_priority": high_priority,
        "overdue": overdue,
    }


def get_overdue_tasks():
    """
    Returns a QuerySet of tasks that have passed their due_date
    and have not yet been marked as DONE.
    """
    today = date.today()
    return Task.objects.filter(
        due_date__lt=today
    ).exclude(status=TaskStatus.DONE)


def mark_task_as_done(task_id: int) -> Task:
    """
    Business logic helper to mark a task as DONE.
    Raises Task.DoesNotExist if task_id does not exist.
    """
    task = Task.objects.get(pk=task_id)
    task.status = TaskStatus.DONE
    task.save(update_fields=['status', 'updated_at'])
    return task
