# Generated by Django 2.2 on 2019-04-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0046_auto_20190425_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagesection',
            name='type',
            field=models.CharField(choices=[('not_configured', 'not_configured'), ('triple_headliner_img', 'triple_headliner_img'), ('carousel', 'carousel'), ('side_image_headliner', 'side_image_headliner'), ('raw_html', 'raw_html'), ('custom_template', 'custom_template')], default='not_configured', max_length=64),
        ),
    ]
