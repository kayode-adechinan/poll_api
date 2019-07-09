from rest_framework import permissions

#Authenticated users can create choices only for polls they have created.
#Authenticated users can delete only polls they have created.

class CanEditPost(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.created_by == request.user


class CanEditChoice(permissions.BasePermission):
   
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.poll.created_by == request.user


class IsOwnerOrReadOnly(permissions.BasePermission):
   
    def has_permission(self, request, view):
        return False

          