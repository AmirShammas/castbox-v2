from django.contrib import admin
from django.contrib.admin import register
from .models import Comment


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "channel", "is_active",)
    list_editable = ("is_active",)
