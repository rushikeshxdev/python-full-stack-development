from django.db import models
from .constants import TaskStatus, TaskPriority
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, default="")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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



class Task(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when task was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when task was last updated")

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
