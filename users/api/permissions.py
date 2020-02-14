from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return True

    def has_obj_permission(self, request, view, obj):
        return True

