# Generated by Django 3.2.16 on 2024-03-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_sdk_gender_birth_nation'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='card_profile_image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Card Profile Image URL'),
        ),
    ]
