# filepath: /D:/projects/django_project/SMUMSJ/accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username',
                    'first_name', 'last_name', 'is_staff', 'role']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {
         'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Role', {'fields': ('role',)}),  # Add the role field here
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            # Add the role field here
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone', 'role'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
