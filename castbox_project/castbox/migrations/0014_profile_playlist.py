# Generated by Django 4.2 on 2024-04-26 22:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("castbox", "0013_playlist"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="playlist",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="profiles",
                to="castbox.playlist",
                verbose_name="Playlists",
            ),
        ),
    ]
