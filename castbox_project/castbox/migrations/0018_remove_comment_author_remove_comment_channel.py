# Generated by Django 4.2 on 2024-05-03 17:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("castbox", "0017_alter_comment_channel_alter_episode_channel_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="author",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="channel",
        ),
    ]
