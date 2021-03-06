# Generated by Django 2.2 on 2019-05-08 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0037_remove_productpromotion_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(blank=True, null=True)),
                ('creation_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_changed_timestamp', models.DateTimeField(auto_now=True)),
                ('job_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
