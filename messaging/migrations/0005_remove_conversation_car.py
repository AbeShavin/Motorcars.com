# Generated by Django 5.0.6 on 2024-07-30 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("messaging", "0004_conversation_car"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="conversation",
            name="car",
        ),
    ]
