# Generated by Django 5.0.6 on 2024-07-23 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_listing", "0010_alter_car_vin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="make",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="car",
            name="model",
            field=models.CharField(max_length=50),
        ),
    ]
