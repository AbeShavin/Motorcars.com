# Generated by Django 5.0.6 on 2024-07-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("car_listing", "0004_carimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="make",
            field=models.CharField(
                choices=[
                    ("Acura", "Acura"),
                    ("Audi", "Audi"),
                    ("BMW", "BMW"),
                    ("Buick", "Buick"),
                    ("Cadillac", "Cadillac"),
                    ("Chevrolet", "Chevrolet"),
                    ("Chrysler", "Chrysler"),
                    ("Dodge", "Dodge"),
                    ("Datsun", "Datsun"),
                    ("Eagle", "Eagle"),
                    ("Ford", "Ford"),
                    ("GMC", "GMC"),
                    ("Honda", "Honda"),
                    ("Hyundai", "Hyundai"),
                    ("Infiniti", "Infinity"),
                    ("Isuzu", "Isuzu"),
                    ("Jaguar", "Jaguar"),
                    ("Kia", "Kia"),
                    ("Lexus", "Lexus"),
                    ("Mercedes Benz", "Mercedes Benz"),
                    ("Nissan", "Nissan"),
                    ("Oldsmobile", "Oldsmobile"),
                    ("Pontiac", "Pontiac"),
                    ("Porsche", "Porsche"),
                    ("Toyota", "Toyota"),
                    ("Volkswagen", "Volkswagen"),
                ],
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="model",
            field=models.CharField(
                choices=[
                    ("Camry", "Camry"),
                    ("Corolla", "Corolla"),
                    ("A4", "A4"),
                    ("Grand National", "Grand National"),
                    ("Civic", "Civic"),
                    ("Q45", "Q45"),
                    ("911 Turbo", "911 Turbo"),
                    ("F-150", "F-150"),
                    ("Silverado", "Silverdao"),
                ],
                max_length=50,
            ),
        ),
    ]
