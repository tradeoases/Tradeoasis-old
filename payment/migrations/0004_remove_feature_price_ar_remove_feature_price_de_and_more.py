# Generated by Django 4.0 on 2023-06-03 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_alter_membershipplan_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feature',
            name='price_ar',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='price_de',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='price_fr',
        ),
    ]
