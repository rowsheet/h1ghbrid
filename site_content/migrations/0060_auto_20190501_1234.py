# Generated by Django 2.2 on 2019-05-01 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0059_auto_20190501_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customtemplaterow',
            name='result_type',
            field=models.CharField(choices=[('table', 'table'), ('json_array', 'json_array'), ('json_object_agg', 'json_object_agg')], default='table', max_length=32),
        ),
    ]