from rest_framework.permissions import BasePermission


class IsAdminOrRelatedUserCanDelete(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser or request.user == obj.user:
            return True
        return False
