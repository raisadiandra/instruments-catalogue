# Generated by Django 4.2.5 on 2023-09-11 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_product_items'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Items',
            new_name='Item',
        ),
    ]
