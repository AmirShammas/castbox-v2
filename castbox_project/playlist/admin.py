from django.contrib import admin
from django.contrib.admin import register
from .models import Playlist


@register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "user", "is_active",)
    list_editable = ("is_active",)
