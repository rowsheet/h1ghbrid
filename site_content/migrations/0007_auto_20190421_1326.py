# Generated by Django 2.2 on 2019-04-21 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0006_auto_20190421_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='title',
            field=models.CharField(default=None, max_length=64, unique=True),
        ),
    ]