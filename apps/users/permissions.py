from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """Разрешение только для администраторов"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "admin")
    
class IsFkj(permissions.BasePermission):
    """Разрешение только для ФКЖ"""
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == "fkj")

class IsFkjOrReadOnly(permissions.BasePermission):
    """Разрешает чтение всем, а изменение только ФКЖ"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.role == "fkj")