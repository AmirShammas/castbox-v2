from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.base_model import MyBaseModel
from channel.models import Channel
from comment.models import Comment
from follow.models import Follow
from episode.models import Episode
from like.models import Like


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
        ordering = ("id",)


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


@receiver(post_save, sender=CustomUser)
def create_default_playlist(sender, instance, created, **kwargs):
    if created:
        new_playlist = Playlist.objects.create(
            user=instance, title="default-playlist")
        profile = Profile.objects.get(owner=instance)
        profile.playlist.add(new_playlist)


@receiver(post_save, sender=Episode)
def create_episode_mention(sender, instance, created, **kwargs):
    if created:
        for follow in instance.channel.follows.all():
            new_mention = Mention.objects.create(
                user=follow.user, message=f"A new episode '{instance.title}' created in channel '{instance.channel.title}' !!", channel=instance.channel, episode=instance)
            profile = Profile.objects.get(owner=follow.user)
            profile.mention.add(new_mention)


class Mention(MyBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True,
                             on_delete=models.CASCADE, related_name="mentions", verbose_name="User")
    message = models.TextField(null=True, blank=True, verbose_name="Message")
    channel = models.ForeignKey(Channel, null=True, blank=True,
                                on_delete=models.CASCADE, related_name="mentions", verbose_name="Channel")
    episode = models.ForeignKey(Episode, null=True, blank=True,
                                on_delete=models.CASCADE, related_name="mentions", verbose_name="Episode")

    class Meta:
        verbose_name = "Mention"
        verbose_name_plural = "Mentions"
        ordering = ("id",)

    def __str__(self):
        return str(self.id)


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

