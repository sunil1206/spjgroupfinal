# Generated by Django 4.1 on 2023-03-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="requestcard",
            fields=[
                ("name", models.CharField(max_length=25)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("Female", "Female")], max_length=10
                    ),
                ),
                ("email", models.EmailField(max_length=100)),
                ("phone", models.IntegerField()),
                ("address", models.CharField(max_length=25)),
                ("post", models.IntegerField()),
                ("aadhar_card", models.IntegerField(primary_key=True, serialize=False)),
                ("ration_number", models.IntegerField()),
                (
                    "purpose",
                    models.CharField(
                        choices=[
                            ("Enquiry", "Enquiry"),
                            ("Apply", "Apply"),
                            ("Complient", "Complient"),
                            ("Others", "Others"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
    ]