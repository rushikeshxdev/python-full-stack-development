from rest_framework import serializers


class TaskMetricsSerializer(serializers.Serializer):
    total = serializers.IntegerField(help_text="Total number of tasks")
    completed = serializers.IntegerField(help_text="Number of completed tasks")
    in_progress = serializers.IntegerField(help_text="Number of tasks in progress")
    todo = serializers.IntegerField(help_text="Number of todo tasks")
    high_priority = serializers.IntegerField(help_text="Number of high priority tasks")
    overdue = serializers.IntegerField(help_text="Number of overdue tasks")
