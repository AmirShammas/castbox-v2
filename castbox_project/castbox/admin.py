from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register
from .models import Channel, Comment, Episode


CustomUser = get_user_model()
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("id", "username", "email", "is_superuser",)
admin.site.register(CustomUser, CustomUserAdmin)


@register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "is_active",)
    list_editable = ("is_active",)


@register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "channel", "is_active",)
    list_editable = ("is_active",)


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "channel", "is_active",)
    list_editable = ("is_active",)


