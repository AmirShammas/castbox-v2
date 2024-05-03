from django.contrib import admin
from django.contrib.admin import register
from .models import Follow


@register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "channel", "is_active",)
    list_editable = ("is_active",)
