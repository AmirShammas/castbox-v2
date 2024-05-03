from django.contrib import admin
from django.contrib.admin import register
from .models import Mention


@register(Mention)
class MentionAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "channel",
                    "episode", "message", "is_active",)
    list_editable = ("is_active",)
