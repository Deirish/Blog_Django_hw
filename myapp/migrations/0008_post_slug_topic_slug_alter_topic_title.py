# Generated by Django 4.2 on 2023-04-24 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_post_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='topic',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Topic'),
        ),
    ]
