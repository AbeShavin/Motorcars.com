# Generated by Django 5.0.6 on 2024-08-13 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("messaging", "0010_chatsession_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="chatsession",
            name="initiator",
        ),
        migrations.RemoveField(
            model_name="chatsession",
            name="receiver",
        ),
        migrations.DeleteModel(
            name="ChatMessage",
        ),
        migrations.DeleteModel(
            name="ChatSession",
        ),
    ]
