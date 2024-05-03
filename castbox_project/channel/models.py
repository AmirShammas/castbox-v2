from django.db import models
from django.conf import settings
from utils.base_model import MyBaseModel


class Channel(MyBaseModel):
    title = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name="Title")
    description = models.TextField(
        null=True, blank=True, verbose_name="Description")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                              on_delete=models.CASCADE, related_name="channels", verbose_name="Owner")

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"
        ordering = ("id",)

    def __str__(self):
        return self.title

