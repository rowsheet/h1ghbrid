# Generated by Django 2.2 on 2019-05-08 05:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tgtree', '0046_auto_20190508_0523'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usermembership',
            unique_together={('user', 'plan')},
        ),
    ]