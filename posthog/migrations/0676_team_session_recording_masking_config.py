# Generated by Django 4.2.18 on 2025-02-26 11:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0675_add_playlist_viewed"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="session_recording_masking_config",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
