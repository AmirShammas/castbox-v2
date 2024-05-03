from django.db import models
from django.conf import settings
from utils.base_model import MyBaseModel
from channel.models import Channel


class Follow(MyBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                             on_delete=models.CASCADE, related_name="follows", verbose_name="User")
    channel = models.ForeignKey(Channel, null=True, blank=True,
                                on_delete=models.CASCADE, related_name="follows", verbose_name="Channel")

    class Meta:
        verbose_name = "Follow"
        verbose_name_plural = "Follows"
        ordering = ("id",)

    def __str__(self):
        return str(self.id)
