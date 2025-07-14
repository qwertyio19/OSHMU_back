from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAdminOrReadOnly(BasePermission):
    """
    Разрешает только чтение (GET, HEAD, OPTIONS) всем,
    но создание/изменение/удаление — только админу.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role == 'admin'
    



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




class IsAdminOrReadOnly(permissions.BasePermission):
    """Разрешает чтение всем, а изменение только Админ"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_authenticated and request.user.role == "admin")




class FKJOnlyWritePermission(permissions.BasePermission):
    """
    - Только пользователи с ролью FKJ могут создавать и изменять практики.
    - Остальные (включая студентов и супер-админов) имеют только чтение (SAFE_METHODS).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and getattr(request.user, 'role', '') == 'fkj'




class IsAdminOrFkjExceptCreate(permissions.BasePermission):
    """
    - Админ может делать всё.
    - ФКЖ может всё, кроме создания (POST).
    - Остальные — ничего не могут, даже читать.
    """

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        # Админ может всё
        if user.role == 'admin':
            return True

        # ФКЖ может всё, кроме создания (POST)
        if user.role == 'fkj' and request.method != 'POST':
            return True

        return False