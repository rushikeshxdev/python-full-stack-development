from datetime import date
from django.db import transaction
from django.db.models import Count, Q, F
from .models import Task, Project
from .constants import TaskStatus, TaskPriority


def get_task_metrics(user=None):
    queryset = Task.objects.all()
    if user:
        queryset = queryset.for_user(user)

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
    return Task.objects.overdue()


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


def get_heavy_performance_report(use_cache: bool = True) -> dict:
    """
    Computes system-wide performance metrics using the Cache-Aside pattern.
    If cached in Redis: returns in ~2ms (from_cache=True).
    If cache miss: runs heavy computation, saves to Redis with 5-minute TTL, and returns.
    """
    import time
    from django.utils import timezone
    from django.contrib.auth.models import User
    from .cache import get_cached_performance_report, set_cached_performance_report

    # 1. Check Redis Cache First (Cache HIT)
    if use_cache:
        cached_data = get_cached_performance_report()
        if cached_data is not None:
            cached_data['from_cache'] = True
            return cached_data

    # 2. Cache MISS: Execute heavy analytical query & calculations
    start_time = time.perf_counter()

    # System-wide metrics
    total_tasks = Task.objects.count()
    completed_tasks = Task.objects.filter(status=TaskStatus.DONE).count()
    completion_rate = round((completed_tasks / total_tasks * 100), 2) if total_tasks > 0 else 0.0

    # Project velocity breakdown
    project_velocities = []
    for proj in Project.objects.all():
        p_total = proj.tasks.count()
        p_done = proj.tasks.filter(status=TaskStatus.DONE).count()
        velocity = round((p_done / p_total * 100), 2) if p_total > 0 else 0.0
        project_velocities.append({
            'project_id': proj.id,
            'project_name': proj.name,
            'total_tasks': p_total,
            'completed_tasks': p_done,
            'velocity_percent': velocity,
        })

    # Contributor workload distribution
    contributor_workloads = []
    for u in User.objects.filter(is_active=True):
        assigned = Task.objects.filter(assigned_to=u).count()
        high_prio = Task.objects.filter(assigned_to=u, priority=TaskPriority.HIGH).count()
        if assigned > 0:
            contributor_workloads.append({
                'username': u.username,
                'total_assigned': assigned,
                'high_priority_count': high_prio,
            })

    # Simulated intensive statistical modeling calculation
    time.sleep(0.6)

    execution_time_ms = round((time.perf_counter() - start_time) * 1000, 2)

    report_data = {
        'generated_at': timezone.now().isoformat(),
        'execution_time_ms': execution_time_ms,
        'total_tasks': total_tasks,
        'system_completion_rate': completion_rate,
        'project_velocities': project_velocities,
        'contributor_workloads': contributor_workloads,
        'from_cache': False,
    }

    # 3. Store in Redis Cache for 5 minutes (300 seconds)
    if use_cache:
        set_cached_performance_report(report_data)

    return report_data




