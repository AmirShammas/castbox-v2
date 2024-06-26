from django.db import models
from django.conf import settings
from utils.base_model import MyBaseModel
from episode.models import Episode
from channel.models import Channel
from comment.models import Comment
from like.models import Like
from follow.models import Follow
from mention.models import Mention
from playlist.models import Playlist


class Profile(MyBaseModel):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True,
                                 on_delete=models.CASCADE, related_name="profile", verbose_name="Owner")
    channel = models.ManyToManyField(
        Channel, null=True, blank=True, related_name="profiles", verbose_name="Channels")
    episode = models.ManyToManyField(
        Episode, null=True, blank=True, related_name="profiles", verbose_name="Episodes")
    comment = models.ManyToManyField(
        Comment, null=True, blank=True, related_name="profiles", verbose_name="Comments")
    like = models.ManyToManyField(
        Like, null=True, blank=True, related_name="profiles", verbose_name="Likes")
    follow = models.ManyToManyField(
        Follow, null=True, blank=True, related_name="profiles", verbose_name="Follows")
    mention = models.ManyToManyField(
        Mention, null=True, blank=True, related_name="profiles", verbose_name="Mentions")
    playlist = models.ManyToManyField(
        Playlist, null=True, blank=True, related_name="profiles", verbose_name="Playlists")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
        ordering = ("id",)

    def __str__(self):
        return str(self.id)

    def get_comments(self):
        return self.comment.all()

    def get_channels(self):
        return self.channel.all()

    def get_likes(self):
        return self.like.all()

    def get_follows(self):
        return self.follow.all()

    def get_mentions(self):
        return self.mention.all()

    def get_playlists(self):
        return self.playlist.all()
