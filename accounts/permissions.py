from rest_framework import  permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions()) 
        if user.is_staff:
            if user.has_perm('accounts.add_accounts') :
                return True
            if user.has_perm('accounts.delete_accounts') :
                return True
            if user.has_perm('accounts.change_accounts') :
                return True
            if user.has_perm('accounts.view_accounts') :
                return True
            return False
        return False
