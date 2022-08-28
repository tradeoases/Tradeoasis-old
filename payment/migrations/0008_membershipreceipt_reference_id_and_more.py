# Generated by Django 4.0.6 on 2022-08-22 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0007_alter_membershipplan_price"),
    ]

    operations = [
        migrations.AddField(
            model_name="membershipreceipt",
            name="reference_id",
            field=models.CharField(
                blank=True, max_length=20, null=True, verbose_name="reference_id"
            ),
        ),
        migrations.AddField(
            model_name="membershipreceipt",
            name="status",
            field=models.CharField(
                default="NOT APPROVED", max_length=20, verbose_name="status"
            ),
        ),
    ]
