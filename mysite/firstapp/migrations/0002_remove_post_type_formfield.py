# Generated by Django 2.1.1 on 2020-02-21 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_type',
            name='formfield',
        ),
    ]