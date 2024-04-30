from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import register
from .models import Channel, Comment, Episode, Follow, Like, Log, Mention, Playlist, Profile


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


@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "is_active",)
    list_editable = ("is_active",)


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "channel", "episode", "is_active",)
    list_editable = ("is_active",)


@register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "channel", "is_active",)
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


@register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "channel",
                    "episode", "message", "is_active",)
    list_editable = ("is_active",)
