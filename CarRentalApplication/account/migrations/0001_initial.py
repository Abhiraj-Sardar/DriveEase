# Generated by Django 5.0.2 on 2024-03-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=40)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
    ]
