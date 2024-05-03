from django.contrib import admin
from django.contrib.admin import register
from .models import Log


@register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "channel",
                    "episode", "message", "is_active",)
    list_editable = ("is_active",)
