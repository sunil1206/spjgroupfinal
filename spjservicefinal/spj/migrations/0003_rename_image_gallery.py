# Generated by Django 4.1 on 2023-04-06 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("spj", "0002_image_remove_service_detail_img2"),
    ]

    operations = [
        migrations.RenameModel(old_name="Image", new_name="gallery",),
    ]
