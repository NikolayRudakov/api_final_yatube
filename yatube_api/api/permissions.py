from genericpath import exists
from rest_framework import permissions


class Сurrent_User_Or_Read_Only(permissions.BasePermission):
    message = 'Доступно только текущуму пользователю.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.author:
            current_user = obj.author
        else:
            current_user = obj.user
        return current_user == request.user
