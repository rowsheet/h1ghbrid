# Generated by Django 2.2.1 on 2019-05-14 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='product',
            name='htc_number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='man_part_number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='model',
        ),
        migrations.RemoveField(
            model_name='product',
            name='msrp',
        ),
        migrations.RemoveField(
            model_name='product',
            name='spec_kv',
        ),
        migrations.RemoveField(
            model_name='product',
            name='text_document',
        ),
    ]
