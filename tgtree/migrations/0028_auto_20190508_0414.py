# Generated by Django 2.2 on 2019-05-08 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0027_auto_20190508_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='adult_use_item_name',
            new_name='name',
        ),
    ]
