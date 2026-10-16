from django.db import models
from django.db.models import Q
from django.utils import timezone
from .constants import TaskStatus, TaskPriority
from django.contrib.auth.models import User

class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Project(TimestampModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"#{self.name}"

class TaskQuerySet(models.QuerySet):
    def completed(self):
        return self.filter(status=TaskStatus.DONE)

    def in_progress(self):
        return self.filter(status=TaskStatus.IN_PROGRESS)

    def todo(self):
        return self.filter(status=TaskStatus.TODO)
    
    def overdue(self):
        return self.filter(due_date__lt=timezone.now().date()).exclude(status=TaskStatus.DONE)
    
    def high_priority(self):
        return self.filter(priority=TaskPriority.HIGH)
    
    def medium_priority(self):
        return self.filter(priority=TaskPriority.MEDIUM)
    
    def low_priority(self):
        return self.filter(priority=TaskPriority.LOW)
    
    def for_user(self, user):
        return self.filter(Q(owner=user) | Q(assigned_to=user))
    
    def with_project(self, project):
        return self.filter(project=project)
    
    def with_tag(self, tag):
        return self.filter(tags__name=tag)
    
    def search(self, query):
        return self.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )


class Task(TimestampModel):
    objects = TaskQuerySet.as_manager()

    title = models.CharField(max_length=200, help_text="Title of the task")
    description = models.TextField(blank=True, default="", help_text="Detailed description of the task")
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
        help_text="Current status"
    )
    priority = models.CharField(
        max_length=10,
        choices=TaskPriority.choices,
        default=TaskPriority.MEDIUM,
        help_text="Priority level"
    )
    due_date = models.DateField(null=True, blank=True, help_text="Optional completion deadline (YYYY-MM-DD)")

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tasks',
        help_text="Owner of the task"
    )

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_tasks',
        help_text="User assigned to execute the task"
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tasks'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='tasks')

    class Meta:

        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        indexes = [
            models.Index(fields=['status'], name='task_status_idx'),
            models.Index(fields=['due_date'], name='task_due_date_idx'),
            models.Index(fields=['created_at'], name='task_created_at_idx'),
            models.Index(fields=['owner', 'status'], name='task_owner_status_idx'),
        ]

    def __str__(self):
        return f"[{self.status}] {self.title}"


class Notification(models.Model):
    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notifications',
        help_text="User who receives the notification"
    )
    actor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='triggered_notifications',
        help_text="User who triggered the notification"
    )
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications',
        help_text="Related task"
    )
    verb = models.CharField(max_length=255, help_text="Action description (e.g. 'assigned you to task')")
    is_read = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['recipient', 'is_read'], name='notif_recipient_read_idx'),
        ]

    def __str__(self):
        actor_name = self.actor.username if self.actor else "System"
        return f"To {self.recipient.username}: {actor_name} {self.verb}"

