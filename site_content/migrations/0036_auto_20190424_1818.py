# Generated by Django 2.2 on 2019-04-24 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cloud_storage', '0011_auto_20190424_1453'),
        ('site_content', '0035_auto_20190424_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='SideImageHeadliner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=64, unique=True)),
                ('title_2', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('align', models.CharField(choices=[('text-left', 'Left'), ('text-right', 'Right')], default='text-left', max_length=16)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
                ('img_src', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='SideImageHeadliner_img_src', to='cloud_storage.CloudFile')),
                ('section', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='site_content.Section')),
            ],
        ),
        migrations.DeleteModel(
            name='HeadlinerImg',
        ),
    ]