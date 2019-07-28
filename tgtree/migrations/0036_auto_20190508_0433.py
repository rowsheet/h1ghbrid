# Generated by Django 2.2 on 2019-05-08 04:33

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0035_auto_20190508_0426'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductPromotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('title', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='End Date')),
                ('promo_code', models.CharField(blank=True, default=None, max_length=32, null=True, unique=True)),
                ('image_url', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('selling_price', models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6, null=True)),
                ('discount', models.FloatField(default=0.5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(1.0)])),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_changed_timestamp', models.DateTimeField(auto_now=True)),
                ('job_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPromotionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_changed_timestamp', models.DateTimeField(auto_now=True)),
                ('job_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='meddeal',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='recdeal',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='DailyDeal',
        ),
        migrations.DeleteModel(
            name='MedDeal',
        ),
        migrations.DeleteModel(
            name='RecDeal',
        ),
        migrations.AddField(
            model_name='productpromotion',
            name='category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tgtree.ProductPromotionCategory'),
        ),
        migrations.AddField(
            model_name='productpromotion',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tgtree.Product'),
        ),
    ]