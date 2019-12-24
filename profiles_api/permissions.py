from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    # def __init__(self, arg):
    #     super(UpdateOwnProfile, self).__init__()
    #     self.arg = arg

    def has_object_permission(self, request, view, obj):
        """Check user is treying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
        
