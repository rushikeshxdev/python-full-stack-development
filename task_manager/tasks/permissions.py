from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff


class TaskRolePermission(permissions.BasePermission):
    """
    Day 14: Role-Based Access Control (RBAC).
    Uses Django auth Groups: 'Admin', 'Contributor', 'Viewer'.

    1. Admin (or is_staff):
       Full access to all operations (read, create, edit, delete any task).
    2. Contributor (default for authenticated users):
       Can read, create tasks, and edit/delete ONLY their own tasks.
    3. Viewer:
       Read-only (GET, HEAD, OPTIONS). Blocked with 403 on POST, PUT, PATCH, DELETE.
    """
    message = "You do not have permission to perform this action based on your role."

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        # Read methods (GET, HEAD, OPTIONS) allowed for all authenticated roles
        if request.method in permissions.SAFE_METHODS:
            return True

        # Admins have full access to all write operations
        if request.user.is_staff or request.user.groups.filter(name='Admin').exists():
            return True

        # Viewers cannot perform any write operation (POST, PUT, PATCH, DELETE)
        if request.user.groups.filter(name='Viewer').exists():
            self.message = "Viewers have read-only access and cannot create or modify tasks."
            return False

        # Contributors can create tasks
        return True

    def has_object_permission(self, request, view, obj):
        # Read methods allowed for all authenticated users
        if request.method in permissions.SAFE_METHODS:
            return True

        # Admins can modify or delete any task
        if request.user.is_staff or request.user.groups.filter(name='Admin').exists():
            return True

        # Viewers cannot modify tasks
        if request.user.groups.filter(name='Viewer').exists():
            return False

        # Contributors can only edit or delete their own tasks
        return obj.owner == request.user