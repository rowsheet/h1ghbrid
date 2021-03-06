# Generated by Django 2.2 on 2019-05-01 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_content', '0056_auto_20190501_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextBitCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=64, unique=True)),
                ('creation_timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='textbit',
            name='text_bit_category',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='text_bit_category', to='site_content.TextBitCategory'),
        ),
    ]
