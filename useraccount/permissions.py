from rest_framework import permissions

class SuperUserorOwnerorReadOnly(permissions.BasePermission):
    """" Object-level permission to only allow owners or superuser or staff of an object to edit it. """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id or request.user.is_superuser or request.user.is_staff