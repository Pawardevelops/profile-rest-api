from rest_framework import permissions

class BaseOwnerPermission(permissions.BasePermission):
    """Base permission to allow owners to edit their own objects"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own object"""
        if request.method in permissions.SAFE_METHODS:
            return True
            
        return self.is_owner(request, view, obj)

    def is_owner(self, request, view, obj):
        """Override this method to define ownership logic"""
        raise NotImplementedError("Subclasses must implement is_owner")


class UpdateOwnProfile(BaseOwnerPermission):
    """Allow users to update their own profile"""
    
    def is_owner(self, request, view, obj):
        return obj.id == request.user.id


class UpdateOwnStatus(BaseOwnerPermission):
    """Allow users to update their own status"""
    
    def is_owner(self, request, view, obj):
        return obj.user_profile.id == request.user.id