# Generated by Django 2.2 on 2019-05-01 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0051_auto_20190501_0840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomScripts',
            new_name='CustomScript',
        ),
    ]