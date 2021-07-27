# core/permissions.py
from rest_framework import permissions


class IsCreatorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        ''' Don't allow unauthicated users access to all resources '''
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        '''Allow super user access to all resources'''
        if request.user.is_superuser:
            return True
            
        ''' Read-only permissions are allowed for any request'''
        if request.method in permissions.SAFE_METHODS:
            return True

        ''' Write permissions are only allowed to the creator of a resource'''
        return obj.created_by == request.user
