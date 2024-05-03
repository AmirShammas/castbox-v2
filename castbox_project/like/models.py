from django.db import models
from django.conf import settings
from utils.base_model import MyBaseModel
from channel.models import Channel
from episode.models import Episode


class Like(MyBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                             on_delete=models.CASCADE, related_name="likes", verbose_name="User")
    channel = models.ForeignKey(Channel, null=True, blank=True,
                                on_delete=models.CASCADE, related_name="likes", verbose_name="Channel")
    episode = models.ForeignKey(Episode, null=True, blank=True,
                                on_delete=models.CASCADE, related_name="likes", verbose_name="Episode")

    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        ordering = ("id",)

    def __str__(self):
        return str(self.id)
