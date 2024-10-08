# Generated by Django 5.0.6 on 2024-08-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_listing", "0017_alter_car_mileage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="car",
            name="zipcode",
            field=models.CharField(default="00000", max_length=5),
        ),
    ]
