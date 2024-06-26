from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id", "username", "email", "is_superuser",)


admin.site.register(CustomUser, CustomUserAdmin)
