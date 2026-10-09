from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from tasks.services import get_task_metrics
from tasks.models import Task, Project, Tag


class Command(BaseCommand):
    help = "Generates a clean terminal summary of tasks, projects, and metrics across the system."

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            type=str,
            help='Filter metrics for a specific user username.',
            default=None
        )

    def handle(self, *args, **options):
        username = options.get('username')
        user = None

        if username:
            try:
                user = User.objects.get(username=username)
                self.stdout.write(self.style.NOTICE(f"\n=== Task Manager Summary for user: @{username} ==="))
            except User.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"User '@{username}' does not exist."))
                return
        else:
            self.stdout.write(self.style.MIGRATE_HEADING("\n=== Task Manager System-Wide Summary ==="))

        metrics = get_task_metrics(user=user)

        self.stdout.write("-" * 50)
        self.stdout.write(f"  Total Projects:   {Project.objects.count()}")
        self.stdout.write(f"  Total Tags:       {Tag.objects.count()}")
        self.stdout.write(f"  Total Tasks:      {metrics.get('total', 0)}")
        self.stdout.write(self.style.SUCCESS(f"  [DONE] Completed:  {metrics.get('completed', 0)}"))
        self.stdout.write(self.style.WARNING(f"  [PROG] In Progress:{metrics.get('in_progress', 0)}"))
        self.stdout.write(self.style.NOTICE(f"  [TODO] To Do:      {metrics.get('todo', 0)}"))
        self.stdout.write(f"  High Priority:    {metrics.get('high_priority', 0)}")

        overdue = metrics.get('overdue', 0)
        if overdue > 0:
            self.stdout.write(self.style.ERROR(f"  [WARN] Overdue:   {overdue}"))
        else:
            self.stdout.write(self.style.SUCCESS(f"  [OK]   Overdue:   0"))
        self.stdout.write("-" * 50 + "\n")
