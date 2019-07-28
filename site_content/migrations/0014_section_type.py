# Generated by Django 2.2 on 2019-04-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0013_auto_20190421_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='type',
            field=models.CharField(choices=[('triple_headliner_img', 'triple_headliner_img'), ('triple_headliner_text', 'triple_headliner_text'), ('jumbotron', 'jumbotron'), ('carousel', 'carousel'), ('headline_left', 'headline_left'), ('headline_right', 'headline_right')], default='not_configured', max_length=64),
        ),
    ]