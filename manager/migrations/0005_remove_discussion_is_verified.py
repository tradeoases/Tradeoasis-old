# Generated by Django 4.0 on 2023-03-11 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_discussion_is_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='is_verified',
        ),
    ]
