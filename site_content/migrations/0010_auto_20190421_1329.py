# Generated by Django 2.2 on 2019-04-21 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0009_auto_20190421_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(default=None, max_length=64, unique=True),
        ),
    ]
