# Generated by Django 2.1.1 on 2020-02-22 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_remove_post_type_formfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='community_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AddField(
            model_name='post_type',
            name='post_type_slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
