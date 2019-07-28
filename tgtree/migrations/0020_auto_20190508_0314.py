# Generated by Django 2.2 on 2019-05-08 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0019_budtenderqa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailydeal',
            name='promo_code',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='dailydeal',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='meddeal',
            name='promo_code',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='meddeal',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recdeal',
            name='promo_code',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='recdeal',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]