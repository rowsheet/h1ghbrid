# Generated by Django 2.2 on 2019-04-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_storage', '0005_auto_20190424_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudfile',
            name='tags',
            field=models.ManyToManyField(blank=True, to='cloud_storage.CloudFileTag'),
        ),
    ]
