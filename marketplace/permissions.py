from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # Anyone can view products
        if request.method in SAFE_METHODS:
            return True
        # Only logged-in users can create
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Anyone can read
        if request.method in SAFE_METHODS:
            return True
        # Admin can modify anything
        if request.user.is_staff:
            return True
        # Owner can update/delete their product
        return obj.farmer == request.user