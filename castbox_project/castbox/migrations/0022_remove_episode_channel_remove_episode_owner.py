# Generated by Django 4.2 on 2024-05-03 18:51

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("castbox", "0021_alter_profile_follow_delete_follow"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="episode",
            name="channel",
        ),
        migrations.RemoveField(
            model_name="episode",
            name="owner",
        ),
    ]
