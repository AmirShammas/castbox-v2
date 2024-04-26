# Generated by Django 4.2 on 2024-04-26 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("castbox", "0009_follow_profile_follow"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mention",
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
                        related_name="mentions",
                        to="castbox.channel",
                        verbose_name="Channel",
                    ),
                ),
                (
                    "episode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mentions",
                        to="castbox.episode",
                        verbose_name="Episode",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mentions",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Mention",
                "verbose_name_plural": "Mentions",
                "ordering": ("id",),
            },
        ),
        migrations.AddField(
            model_name="profile",
            name="mention",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="profiles",
                to="castbox.mention",
                verbose_name="Mentions",
            ),
        ),
    ]
