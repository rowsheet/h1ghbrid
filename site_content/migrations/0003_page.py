# Generated by Django 2.2 on 2019-04-21 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0002_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='home', max_length=64, unique=True)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
                ('section_eight', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_eight', to='site_content.Section')),
                ('section_five', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_five', to='site_content.Section')),
                ('section_four', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_four', to='site_content.Section')),
                ('section_nine', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_nine', to='site_content.Section')),
                ('section_one', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_one', to='site_content.Section')),
                ('section_seven', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_seven', to='site_content.Section')),
                ('section_six', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_six', to='site_content.Section')),
                ('section_three', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_three', to='site_content.Section')),
                ('section_two', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='section_two', to='site_content.Section')),
            ],
        ),
    ]