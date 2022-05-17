from django.contrib import admin

from agent.models import User
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = User
    serach_fields = ('email', 'first_name', 'last_name', 'slug')
    ordering = ('-created',)
    list_display = ('first_name', 'email', 'is_staff', 'is_active',)

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'slug',)}),
        ('Premissions', {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions',)}),
        ('Personal', {'fields': ('mobile', 'image')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name','slug', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'mobile', 'image')}
        ),
    )



admin.site.register(User, UserAdminConfig)