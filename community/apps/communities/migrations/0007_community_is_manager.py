# Generated by Django 3.2.16 on 2023-12-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0006_alter_community_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='Is Manager'),
        ),
    ]
