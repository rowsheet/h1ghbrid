# Generated by Django 2.2 on 2019-05-01 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0052_auto_20190501_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default=None, max_length=64, unique=True)),
                ('val', models.TextField(blank=True, null=True)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
