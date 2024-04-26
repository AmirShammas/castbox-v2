from django.db import models
from django.contrib.auth.models import AbstractUser
from abc import abstractmethod
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
        ordering = ("id",)

   
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


class MyBaseModel(models.Model):
    is_active = models.BooleanField(
        default=False,
        verbose_name="Is Active",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
    )

    class Meta:
        abstract = True
        ordering = ("pk",)

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("Implement __str__ method")


class Channel(MyBaseModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="Title")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="channels", verbose_name="Owner")

    class Meta:
        verbose_name = "Channel"
        verbose_name_plural = "Channels"
        ordering = ("id",)

    def __str__(self):
        return self.title


class Episode(MyBaseModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="Title")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="episodes", verbose_name="Owner")
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE, related_name="episodes", verbose_name="Channel")

    class Meta:
        verbose_name = "Episode"
        verbose_name_plural = "Episodes"
        ordering = ("id",)

    def __str__(self):
        return self.title


@receiver(post_save, sender=Episode)
def create_episode_mention(sender, instance, created, **kwargs):
    if created:
        for follow in instance.channel.follows.all():
            new_mention = Mention.objects.create(user=follow.user, message=f"A new episode '{instance.title}' created in channel '{instance.channel.title}' !!", channel=instance.channel, episode=instance)
            profile = Profile.objects.get(owner=follow.user)
            profile.mention.add(new_mention)


class Comment(MyBaseModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="Title")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="comments", verbose_name="Author")
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE, related_name="comments", verbose_name="Channel")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ("id",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("channel_list")


class Like(MyBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="likes", verbose_name="User")
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE, related_name="likes", verbose_name="Channel")
    episode = models.ForeignKey(Episode, null=True, blank=True, on_delete=models.CASCADE, related_name="likes", verbose_name="Episode")
    class Meta:
        verbose_name = "Like"
        verbose_name_plural = "Likes"
        ordering = ("id",)

    def __str__(self):
        return str(self.id)


class Follow(MyBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="follows", verbose_name="User")
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE, related_name="follows", verbose_name="Channel")
    class Meta:
        verbose_name = "Follow"
        verbose_name_plural = "Follows"
        ordering = ("id",)

    def __str__(self):
        return str(self.id)


class Mention(MyBaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="mentions", verbose_name="User")
    message = models.TextField(null=True, blank=True, verbose_name="Message")
    channel = models.ForeignKey(Channel, null=True, blank=True, on_delete=models.CASCADE, related_name="mentions", verbose_name="Channel")
    episode = models.ForeignKey(Episode, null=True, blank=True, on_delete=models.CASCADE, related_name="mentions", verbose_name="Episode")
    class Meta:
        verbose_name = "Mention"
        verbose_name_plural = "Mentions"
        ordering = ("id",)

    def __str__(self):
        return str(self.id)


class Playlist(MyBaseModel):
    title = models.CharField(max_length=50, null=True, blank=True, verbose_name="Title")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="playlists", verbose_name="User")
    channel = models.ManyToManyField(Channel, null=True, blank=True, related_name="playlists", verbose_name="Channels")
    episode = models.ManyToManyField(Episode, null=True, blank=True, related_name="playlists", verbose_name="Episodes")
    class Meta:
        verbose_name = "Playlist"
        verbose_name_plural = "Playlists"
        ordering = ("id",)

    def __str__(self):
        return self.title


class Profile(MyBaseModel):
    owner = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name="profile", verbose_name="Owner")
    channel = models.ManyToManyField(Channel, null=True, blank=True, related_name="profiles", verbose_name="Channels")
    episode = models.ManyToManyField(Episode, null=True, blank=True, related_name="profiles", verbose_name="Episodes")
    comment = models.ManyToManyField(Comment, null=True, blank=True, related_name="profiles", verbose_name="Comments")
    like = models.ManyToManyField(Like, null=True, blank=True, related_name="profiles", verbose_name="Likes")
    follow = models.ManyToManyField(Follow, null=True, blank=True, related_name="profiles", verbose_name="Follows")
    mention = models.ManyToManyField(Mention, null=True, blank=True, related_name="profiles", verbose_name="Mentions")
    playlist = models.ManyToManyField(Playlist, null=True, blank=True, related_name="profiles", verbose_name="Playlists")

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
