# Generated by Django 4.1.5 on 2023-01-27 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserAccount",
            fields=[
                ("accountNo", models.IntegerField(primary_key=True, serialize=False)),
                ("firstName", models.CharField(max_length=100)),
                ("lastName", models.CharField(max_length=100)),
                ("phoneNo", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("money", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="UserTransaction",
            fields=[
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="%(class)s_sender",
                        serialize=False,
                        to="account.useraccount",
                    ),
                ),
                ("timeSent", models.DateTimeField(verbose_name="Time sent")),
                ("amount", models.IntegerField()),
                (
                    "reciever",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)s_reciever",
                        to="account.useraccount",
                    ),
                ),
            ],
        ),
    ]
