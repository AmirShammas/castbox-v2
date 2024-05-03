# Generated by Django 4.2 on 2024-05-03 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("episode", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("channel", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Log",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="Is Active"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
                (
                    "message",
                    models.TextField(blank=True, null=True, verbose_name="Message"),
                ),
                (
                    "channel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        to="channel.channel",
                        verbose_name="Channel",
                    ),
                ),
                (
                    "episode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        to="episode.episode",
                        verbose_name="Episode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="logs",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Log",
                "verbose_name_plural": "Logs",
                "ordering": ("id",),
            },
        ),
    ]
