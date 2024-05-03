from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register
from .models import Mention, Playlist, Profile


CustomUser = get_user_model()


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id", "username", "email", "is_superuser",)


admin.site.register(CustomUser, CustomUserAdmin)


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "is_active",)
    list_editable = ("is_active",)


@register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "channel",
                    "episode", "message", "is_active",)
    list_editable = ("is_active",)


@register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "is_active",)
    list_editable = ("is_active",)
