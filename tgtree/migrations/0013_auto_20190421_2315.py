# Generated by Django 2.2 on 2019-04-21 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0012_auto_20190421_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6, null=True),
        ),
    ]
