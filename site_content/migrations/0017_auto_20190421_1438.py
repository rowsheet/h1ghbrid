# Generated by Django 2.2 on 2019-04-21 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0016_auto_20190421_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='section',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='site_content.Section'),
        ),
        migrations.CreateModel(
            name='TripleHeadlinerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=64, unique=True)),
                ('img_src_1', models.CharField(default=None, max_length=64, unique=True)),
                ('title_1', models.CharField(default=None, max_length=64, unique=True)),
                ('text_1', models.CharField(default=None, max_length=255, unique=True)),
                ('button_title_1', models.CharField(default=None, max_length=32, unique=True)),
                ('button_link_1', models.CharField(default=None, max_length=255, unique=True)),
                ('img_src_2', models.CharField(default=None, max_length=64, unique=True)),
                ('title_2', models.CharField(default=None, max_length=64, unique=True)),
                ('text_2', models.CharField(default=None, max_length=255, unique=True)),
                ('button_title_2', models.CharField(default=None, max_length=32, unique=True)),
                ('button_link_2', models.CharField(default=None, max_length=255, unique=True)),
                ('img_src_3', models.CharField(default=None, max_length=64, unique=True)),
                ('title_3', models.CharField(default=None, max_length=64, unique=True)),
                ('text_3', models.CharField(default=None, max_length=255, unique=True)),
                ('button_title_3', models.CharField(default=None, max_length=32, unique=True)),
                ('button_link_3', models.CharField(default=None, max_length=255, unique=True)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
                ('section', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='section', to='site_content.Section')),
            ],
        ),
    ]
