# Generated by Django 2.2 on 2019-04-25 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0015_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='adult_use_item_name',
            new_name='adult_use_item_name_temp',
        ),
    ]
