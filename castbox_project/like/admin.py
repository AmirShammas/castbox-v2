from django.contrib import admin
from django.contrib.admin import register
from .models import Like


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "channel", "episode", "is_active",)
    list_editable = ("is_active",)
