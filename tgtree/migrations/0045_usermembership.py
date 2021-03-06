# Generated by Django 2.2 on 2019-05-08 05:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tgtree', '0044_membershipplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='User Membership Start Date')),
                ('end_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='User Membership End Date')),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_changed_timestamp', models.DateTimeField(auto_now=True)),
                ('plan', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tgtree.MembershipPlan')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
