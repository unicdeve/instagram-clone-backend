from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_obj_permission(self, request, view, obj):
        return True


class IsCurrentUserOrReadOnly(permissions.BasePermission):
    message = "You do not have the permission to perform this action."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

