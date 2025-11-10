from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_roles')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'roles')
    fieldsets = UserAdmin.fieldsets + (
        ('Roles', {'fields': ('roles',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Roles', {'fields': ('roles',)}),
    )

    def get_roles(self, obj):
        return ", ".join([role.get_name_display() for role in obj.roles.all()])
    get_roles.short_description = 'Roles'
