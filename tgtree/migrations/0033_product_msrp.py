# Generated by Django 2.2 on 2019-05-08 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0032_auto_20190508_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='msrp',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6, null=True),
        ),
    ]
