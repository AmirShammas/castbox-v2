# Generated by Django 4.2 on 2024-05-03 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("episode", "0001_initial"),
        ("castbox", "0022_remove_episode_channel_remove_episode_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="like",
            name="episode",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="likes",
                to="episode.episode",
                verbose_name="Episode",
            ),
        ),
        migrations.AlterField(
            model_name="log",
            name="episode",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="logs",
                to="episode.episode",
                verbose_name="Episode",
            ),
        ),
        migrations.AlterField(
            model_name="mention",
            name="episode",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="mentions",
                to="episode.episode",
                verbose_name="Episode",
            ),
        ),
        migrations.AlterField(
            model_name="playlist",
            name="episode",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="playlists",
                to="episode.episode",
                verbose_name="Episodes",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="episode",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="profiles",
                to="episode.episode",
                verbose_name="Episodes",
            ),
        ),
        migrations.DeleteModel(
            name="Episode",
        ),
    ]
