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


class UpdateOwnStatus(permissions.BasePermission):
    """Allow user to update their own status"""

    # def __init__(self, arg):
    #     super(UpdateOwnStatus, self).__init__()
    #     self.arg = arg
    def has_object_permission(self, request, view, obj):
        """Check user is treying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
