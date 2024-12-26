# Generated by Django 3.2.16 on 2024-12-19 01:52

import community.apps.posts.models.mixins.image
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_sync_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='blurred_medias_data',
            field=models.JSONField(default=list, verbose_name='Blurred Medias Data'),
        ),
        migrations.AddField(
            model_name='post',
            name='blurred_thumbnail_media_url',
            field=models.URLField(default=community.apps.posts.models.mixins.image.default_thumbnail_image_path, verbose_name='Blurred Thumbnail Media URL'),
        ),
    ]