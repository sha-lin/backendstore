from rest_framework import permissions
from authentication.models import User


class IsStaffPermission(permissions.BasePermission):
    message = "You're not a staff"

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff