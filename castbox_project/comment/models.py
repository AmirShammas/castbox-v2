from django.db import models
from django.conf import settings
from utils.base_model import MyBaseModel
from channel.models import Channel
from django.urls import reverse


class Comment(MyBaseModel):
    title = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name="Title")
    description = models.TextField(
        null=True, blank=True, verbose_name="Description")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                               on_delete=models.CASCADE, related_name="comments", verbose_name="Author")
    channel = models.ForeignKey(Channel, null=True, blank=True,
                                on_delete=models.CASCADE, related_name="comments", verbose_name="Channel")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("id",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("channel_list")

