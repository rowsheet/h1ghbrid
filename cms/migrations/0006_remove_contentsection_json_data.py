# Generated by Django 2.2.1 on 2019-05-13 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_contentsection_json_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentsection',
            name='json_data',
        ),
    ]