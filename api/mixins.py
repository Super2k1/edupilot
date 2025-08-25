from .permissions import IsStaffEditorPermission
from rest_framework import generics, permissions

class StaffEditorPermissionMixin():
    """
    Mixin to apply IsStaffEditorPermission to views.
    """
    permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]