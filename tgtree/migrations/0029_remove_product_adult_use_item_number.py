# Generated by Django 2.2 on 2019-05-08 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0028_auto_20190508_0414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='adult_use_item_number',
        ),
    ]
