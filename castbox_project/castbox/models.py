from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from signals.signals import create_user_profile, create_default_playlist


class CustomUser(AbstractUser):
    class Meta:
        verbose_name = "CustomUser"
        verbose_name_plural = "CustomUsers"
        ordering = ("id",)


post_save.connect(create_user_profile, sender=CustomUser)

post_save.connect(create_default_playlist, sender=CustomUser)

