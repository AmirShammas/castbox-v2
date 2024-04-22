from django.db import models
from django.contrib.auth.models import AbstractUser
from abc import abstractmethod
from django.conf import settings


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
        ordering = ("id",)


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


