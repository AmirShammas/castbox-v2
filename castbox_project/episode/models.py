from django.db import models
from django.conf import settings
from utils.base_model import MyBaseModel
from channel.models import Channel
from django.db.models.signals import post_save


class Episode(MyBaseModel):
    title = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name="Title")
    description = models.TextField(
        null=True, blank=True, verbose_name="Description")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                              on_delete=models.CASCADE, related_name="episodes", verbose_name="Owner")
    channel = models.ForeignKey(Channel, null=True, blank=True,
                                on_delete=models.CASCADE, related_name="episodes", verbose_name="Channel")

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"
        ordering = ("id",)

    def __str__(self):
        return self.title

