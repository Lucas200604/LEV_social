# Generated by Django 4.2.4 on 2023-08-11 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_image_imagepost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageFiles',
        ),
    ]