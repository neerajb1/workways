from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.user.is_authenticated():
            if request.user.is_staff():
                return True
            raise PermissionDenied("You must logged in to see")
        return obj.user == request.user
