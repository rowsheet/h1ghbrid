# Generated by Django 2.2 on 2019-05-01 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0054_auto_20190501_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='aux_section',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='aux_section', to='site_content.PageSection'),
        ),
    ]
