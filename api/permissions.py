from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    """Return True if http method is safe and user logged in / user is staff / user is the owner of the object"""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and bool(request.user and request.user.is_authenticated):
            return True
        return bool(request.user and request.user.is_staff or request.user == obj.user)
