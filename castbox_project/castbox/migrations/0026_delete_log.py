# Generated by Django 4.2 on 2024-05-03 19:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("castbox", "0025_alter_profile_like_delete_like"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Log",
        ),
    ]
