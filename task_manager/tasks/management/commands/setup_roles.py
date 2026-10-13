from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = "Seeds Admin, Contributor, and Viewer groups and provisions test accounts for RBAC testing."

    def handle(self, *args, **options):
        # 1. Create the 3 core RBAC Groups
        admin_group, _ = Group.objects.get_or_create(name='Admin')
        contributor_group, _ = Group.objects.get_or_create(name='Contributor')
        viewer_group, _ = Group.objects.get_or_create(name='Viewer')

        self.stdout.write(self.style.SUCCESS("Groups verified: Admin, Contributor, Viewer."))

        # 2. Provision / configure test users
        users_data = [
            {
                "username": "admin_user",
                "email": "admin@example.com",
                "password": "AdminPass123!",
                "is_staff": True,
                "group": admin_group,
            },
            {
                "username": "contributor_user",
                "email": "contributor@example.com",
                "password": "ContribPass123!",
                "is_staff": False,
                "group": contributor_group,
            },
            {
                "username": "viewer_user",
                "email": "viewer@example.com",
                "password": "ViewerPass123!",
                "is_staff": False,
                "group": viewer_group,
            },
        ]

        for udata in users_data:
            user, created = User.objects.get_or_create(
                username=udata["username"],
                defaults={"email": udata["email"], "is_staff": udata["is_staff"]}
            )
            user.set_password(udata["password"])
            user.is_staff = udata["is_staff"]
            user.save()
            user.groups.clear()
            user.groups.add(udata["group"])

            action = "Created" if created else "Updated"
            self.stdout.write(f"  - {action} [{udata['username']}] with role: {udata['group'].name}")

        # 3. Synchronize existing project users
        if User.objects.filter(username='rushi').exists():
            rushi = User.objects.get(username='rushi')
            rushi.groups.add(admin_group)
            self.stdout.write("  - Added 'rushi' to Admin group.")

        if User.objects.filter(username='sumit').exists():
            sumit = User.objects.get(username='sumit')
            sumit.groups.add(contributor_group)
            self.stdout.write("  - Added 'sumit' to Contributor group.")

        self.stdout.write(self.style.SUCCESS("\nRBAC role provisioning complete. Ready for Swagger testing."))
