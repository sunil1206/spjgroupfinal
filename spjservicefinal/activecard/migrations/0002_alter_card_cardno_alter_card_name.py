# Generated by Django 4.1 on 2023-04-05 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activecard", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="card", name="cardno", field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="card", name="name", field=models.CharField(max_length=50),
        ),
    ]
