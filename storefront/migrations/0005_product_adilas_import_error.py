# Generated by Django 2.2.1 on 2019-07-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0004_auto_20190721_1054'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='adilas_import_error',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
