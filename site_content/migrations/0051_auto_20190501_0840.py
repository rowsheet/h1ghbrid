# Generated by Django 2.2 on 2019-05-01 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0050_customscripts'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='leading_script',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='leading_script', to='site_content.CustomScripts'),
        ),
        migrations.AddField(
            model_name='page',
            name='trailing_script',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trailing_script', to='site_content.CustomScripts'),
        ),
    ]
