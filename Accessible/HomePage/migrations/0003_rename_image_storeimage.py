# Generated by Django 4.2.5 on 2023-10-22 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0002_rename_images_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='StoreImage',
        ),
    ]
