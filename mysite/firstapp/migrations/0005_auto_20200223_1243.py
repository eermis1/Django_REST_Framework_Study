# Generated by Django 2.1.1 on 2020-02-23 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20200223_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='community_slug',
            field=models.SlugField(editable=False, max_length=150, unique=True),
        ),
    ]
