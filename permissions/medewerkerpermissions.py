# from rest_framework.permissions import BasePermission
# from django.contrib.auth.models import Permission
from rest_framework import permissions
# class MyCustomPermission(BasePermission):
#     def __init__(self, arg1):
#         self.arg1 = arg1
#     # def get_permissionID(self):
#     #     permission = Permission.objects.get(codename="view_customuser")
#     #     return permission
#     def has_permission(self, request, view):
#         user = request.user
#         # permission= self.get_permissionID()
#         if user.is_authenticated and user.user_permissions.filter(codename=self.arg1).exists():
#             return True
#         return False

def permission_required(permission_name, raise_exception=False):
    class PermissionRequired(permissions.BasePermission):
        def has_permission(self, request, view):
            user = request.user
        # permission= self.get_permissionID()
            if user.is_authenticated and user.user_permissions.filter(codename=permission_name).exists():
                return True
            return False
    return PermissionRequired