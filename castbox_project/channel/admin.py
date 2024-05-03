from django.contrib import admin
from django.contrib.admin import register
from .models import Channel


@register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "owner", "is_active",)
    list_editable = ("is_active",)

