# Generated by Django 4.2.7 on 2023-11-10 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_catogory_post_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catogory',
            new_name='Category',
        ),
    ]