# Generated by Django 4.2 on 2024-04-26 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("castbox", "0008_profile_like"),
    ]

    operations = [
        migrations.CreateModel(
            name="Follow",
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
                    "channel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follows",
                        to="castbox.channel",
                        verbose_name="Channel",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follows",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Follow",
                "verbose_name_plural": "Follows",
                "ordering": ("id",),
            },
        ),
        migrations.AddField(
            model_name="profile",
            name="follow",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="profiles",
                to="castbox.follow",
                verbose_name="Follows",
            ),
        ),
    ]