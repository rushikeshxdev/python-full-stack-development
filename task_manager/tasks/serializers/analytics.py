from rest_framework import serializers


class TaskMetricsSerializer(serializers.Serializer):
    total = serializers.IntegerField(help_text="Total number of tasks")
    completed = serializers.IntegerField(help_text="Number of completed tasks")
    in_progress = serializers.IntegerField(help_text="Number of tasks in progress")
    todo = serializers.IntegerField(help_text="Number of todo tasks")
    high_priority = serializers.IntegerField(help_text="Number of high priority tasks")
    overdue = serializers.IntegerField(help_text="Number of overdue tasks")


class ProjectVelocitySerializer(serializers.Serializer):
    project_id = serializers.IntegerField()
    project_name = serializers.CharField()
    total_tasks = serializers.IntegerField()
    completed_tasks = serializers.IntegerField()
    velocity_percent = serializers.FloatField()


class ContributorWorkloadSerializer(serializers.Serializer):
    username = serializers.CharField()
    total_assigned = serializers.IntegerField()
    high_priority_count = serializers.IntegerField()


class TaskPerformanceReportSerializer(serializers.Serializer):
    generated_at = serializers.CharField()
    execution_time_ms = serializers.FloatField()
    total_tasks = serializers.IntegerField()
    system_completion_rate = serializers.FloatField()
    project_velocities = ProjectVelocitySerializer(many=True)
    contributor_workloads = ContributorWorkloadSerializer(many=True)
    from_cache = serializers.BooleanField(default=False)

