# Generated by Django 4.2.5 on 2023-10-26 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0007_alter_storeimage_cannyimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreCannyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cannyimg', models.ImageField(upload_to='cannyImgs/')),
            ],
        ),
        migrations.RemoveField(
            model_name='storeimage',
            name='cannyimg',
        ),
    ]
