from django.contrib import admin
from django.contrib.admin import register
from .models import Episode


@register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "channel", "is_active",)
    list_editable = ("is_active",)
