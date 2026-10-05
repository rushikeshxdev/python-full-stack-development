from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'To Do'),
        ('IN_PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ]

    title = models.CharField(max_length=200, help_text="Title of the task")
    description = models.TextField(blank=True, default="", help_text="Detailed description of the task")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='TODO', help_text="Current status")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM', help_text="Priority level")
    due_date = models.DateField(null=True, blank=True, help_text="Optional completion deadline (YYYY-MM-DD)")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when task was created")
    updated_at = models.DateTimeField(auto_now=True, help_text="Timestamp when task was last updated")

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"[{self.status}] {self.title}"
