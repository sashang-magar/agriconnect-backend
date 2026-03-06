from rest_framework import permissions

class IsFarmer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'FARMER' and request.user.is_authenticated #logged in and a farmer
    
class IsBuyer(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'BUYER' and request.user.is_authenticated