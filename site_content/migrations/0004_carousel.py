# Generated by Django 2.2 on 2019-04-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0003_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('text', models.TextField(blank=True, default=None, null=True)),
                ('img_src', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('button_link', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('button_title', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('align', models.CharField(choices=[('text-left', 'Left'), ('text-center', 'Center'), ('text-right', 'Right')], default='text-center', max_length=16)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
