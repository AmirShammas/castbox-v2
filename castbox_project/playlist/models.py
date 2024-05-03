from django.db import models
from django.conf import settings
from utils.base_model import MyBaseModel
from episode.models import Episode


class Playlist(MyBaseModel):
    title = models.CharField(max_length=50, null=True,
                             blank=True, verbose_name="Title")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                             on_delete=models.CASCADE, related_name="playlists", verbose_name="User")
    episode = models.ManyToManyField(
        Episode, null=True, blank=True, related_name="playlists", verbose_name="Episodes")

    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"
        ordering = ("id",)

    def __str__(self):
        return self.title
