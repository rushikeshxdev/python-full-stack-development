from django.db import models
from .constants import TaskStatus, TaskPriority


class Task(models.Model):
    title = models.CharField(max_length=200, help_text="Title of the task")
    description = models.TextField(blank=True, default="", help_text="Detailed description of the task")
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
        help_text="Current lifecycle status (Master Data)"
    )
    priority = models.CharField(
        max_length=10,
        choices=TaskPriority.choices,
        default=TaskPriority.MEDIUM,
        help_text="Priority level (Master Data)"
    )
    due_date = models.DateField(null=True, blank=True, help_text="Optional completion deadline (YYYY-MM-DD)")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when task was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when task was last updated")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"[{self.status}] {self.title}"
