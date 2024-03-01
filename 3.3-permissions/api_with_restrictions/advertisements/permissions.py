from rest_framework import permissions

# Разрешения текущего пользователя
class SuperuserOrAuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        # Безопасные методы разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Пользователь авторизован
        return request.user.is_authenticated


    def has_object_permission(self, request, view, obj):

        # Суперпользователю все разрешено
        if request.user.is_superuser:
            return True

        # Безопасные методы разрешены всем
        if request.method in permissions.SAFE_METHODS:
            return True

        # Создателю объекта разрешены все действия с объектом
        if obj.creator == request.user:
            return True

        return False




