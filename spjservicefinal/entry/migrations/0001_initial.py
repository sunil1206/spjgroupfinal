# Generated by Django 4.1 on 2023-04-05 06:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="entry",
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
                ("name", models.CharField(max_length=25)),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.IntegerField()),
                ("address", models.CharField(max_length=25)),
                ("address2", models.CharField(max_length=25)),
                (
                    "post",
                    models.PositiveIntegerField(
                        validators=[django.core.validators.MaxValueValidator(999999)]
                    ),
                ),
                (
                    "aadhar_card",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(999999999999)
                        ]
                    ),
                ),
                (
                    "ration_number",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(9999999999)
                        ]
                    ),
                ),
            ],
        ),
    ]