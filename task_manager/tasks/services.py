from datetime import date
from django.db import transaction
from django.db.models import Count, Q, F
from .models import Task, Project
from .constants import TaskStatus, TaskPriority


def get_task_metrics(user=None):
    queryset = Task.objects.all()
    if user:
        queryset = queryset.filter(Q(owner=user) | Q(assigned_to=user))

    today = date.today()
    # Single-pass aggregation using conditional counts to avoid multiple queries
    return queryset.aggregate(
        total=Count('id'),
        completed=Count('id', filter=Q(status=TaskStatus.DONE)),
        in_progress=Count('id', filter=Q(status=TaskStatus.IN_PROGRESS)),
        todo=Count('id', filter=Q(status=TaskStatus.TODO)),
        high_priority=Count('id', filter=Q(priority=TaskPriority.HIGH)),
        overdue=Count('id', filter=Q(due_date__lt=today) & ~Q(status=TaskStatus.DONE)),
    )


def get_overdue_tasks():
    today = date.today()
    return Task.objects.filter(
        due_date__lt=today
    ).exclude(status=TaskStatus.DONE)


def mark_task_as_done(task_id: int) -> Task:
    task = Task.objects.get(pk=task_id)
    task.status = TaskStatus.DONE
    task.save(update_fields=['status', 'updated_at'])
    return task


def create_project_with_tasks(owner, project_name: str, task_titles: list[str], description: str = "") -> Project:
    # Roll back project creation if any associated task fails to insert
    with transaction.atomic():

        project = Project.objects.create(
            name=project_name,
            description=description,
            owner=owner
        )
        tasks = [
            Task(title=title, owner=owner, project=project)
            for title in task_titles
        ]
        Task.objects.bulk_create(tasks)
        return project


def get_edited_tasks(user=None):
    """Returns tasks that have been updated after creation."""
    queryset = Task.objects.filter(updated_at__gt=F('created_at'))
    if user and user.is_authenticated:
        queryset = queryset.filter(owner=user)
    return queryset


def get_task_summaries(user=None):
    queryset = Task.objects.only('id', 'title', 'status', 'priority')
    if user and user.is_authenticated:
        queryset = queryset.filter(owner=user)
    return queryset


def get_user_task_ids(user) -> list[int]:
    return list(Task.objects.filter(owner=user).values_list('id', flat=True))


def get_daily_task_creation_counts(user=None) -> list[dict]:
    from django.db.models.functions import TruncDate
    queryset = Task.objects.all()
    if user and user.is_authenticated:
        queryset = queryset.filter(owner=user)
    return list(
        queryset.annotate(created_date=TruncDate('created_at'))
        .values('created_date')
        .annotate(count=Count('id'))
        .order_by('-created_date')
    )


