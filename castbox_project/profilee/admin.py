from django.contrib import admin
from django.contrib.admin import register
from .models import Profile

@register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "owner", "is_active",)
    list_editable = ("is_active",)
