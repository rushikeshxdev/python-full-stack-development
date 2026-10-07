from django.db import models


class TaskStatus(models.TextChoices):
    """
    Master Data: Allowed lifecycle statuses for a task.
    """
    TODO = 'TODO', 'To Do'
    IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
    DONE = 'DONE', 'Done'


class TaskPriority(models.TextChoices):
    """
    Master Data: Allowed priority levels for a task.
    """
    LOW = 'LOW', 'Low'
    MEDIUM = 'MEDIUM', 'Medium'
    HIGH = 'HIGH', 'High'
