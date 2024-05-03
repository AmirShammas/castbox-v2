from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from utils.base_model import MyBaseModel
from channel.models import Channel
from comment.models import Comment
from follow.models import Follow
from episode.models import Episode
from like.models import Like
from mention.models import Mention
from signals.signals import create_user_profile, create_default_playlist


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
        ordering = ("id",)


post_save.connect(create_user_profile, sender=CustomUser)

post_save.connect(create_default_playlist, sender=CustomUser)


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

