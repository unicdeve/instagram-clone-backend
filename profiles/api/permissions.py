from rest_framework import permissions


class IsCurrentUserOrReadOnly(permissions.BasePermission):
    message = "You do not have the permission to perform this action."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user

    def has_permission(self, request, view):
        # print(view.objects.all())
        return True
