# Generated by Django 2.2 on 2019-04-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0026_auto_20190424_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripleheadlinerimage',
            name='text_1',
            field=models.TextField(blank=True, null=True),
        ),
    ]