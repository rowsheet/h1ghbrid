# Generated by Django 2.2 on 2019-05-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0039_productpromotion_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='tgtree.ProductTag'),
        ),
    ]
