from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff


class TaskRolePermission(permissions.BasePermission):
    """
    Role-based permission checking Django groups: Admin, Contributor, Viewer.
    """
    message = "You do not have permission to perform this action based on your role."

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff or request.user.groups.filter(name='Admin').exists():
            return True

        # Viewers are restricted to safe read methods only
        if request.user.groups.filter(name='Viewer').exists():
            self.message = "Viewers have read-only access and cannot create or modify tasks."
            return False

        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_staff or request.user.groups.filter(name='Admin').exists():
            return True

        if request.user.groups.filter(name='Viewer').exists():
            self.message = "Viewers have read-only access and cannot modify or delete tasks."
            return False

        # Contributors cannot delete tasks (even their own tasks)
        if request.method == 'DELETE':
            self.message = "Contributors cannot delete tasks. Deletion is restricted to administrators."
            return False

        # Contributors can only update tasks they personally created
        if obj.owner != request.user:
            self.message = "You can only modify tasks that you personally created."
            return False

        return True


