# Generated by Django 3.2.16 on 2024-07-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0019_merge_20240705_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='title_ar',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='community',
            name='title_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='community',
            name='title_es',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='community',
            name='title_ja',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='community',
            name='title_ko',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='community',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='community',
            name='title_zh_hans',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='community',
            name='title_zh_hant',
            field=models.CharField(max_length=100, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='community',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]
