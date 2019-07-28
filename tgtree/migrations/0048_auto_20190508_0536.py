# Generated by Django 2.2 on 2019-05-08 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tgtree', '0047_auto_20190508_0529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='parent_product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='productpromotion',
            name='category',
        ),
        migrations.RemoveField(
            model_name='productpromotion',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productpromotion',
            name='tags',
        ),
        migrations.AlterUniqueTogether(
            name='usermembership',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='usermembership',
            name='user',
        ),
        migrations.DeleteModel(
            name='EmployeeProductQA',
        ),
        migrations.DeleteModel(
            name='MembershipPlan',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductPromotion',
        ),
        migrations.DeleteModel(
            name='ProductPromotionCategory',
        ),
        migrations.DeleteModel(
            name='ProductTag',
        ),
        migrations.DeleteModel(
            name='UserMembership',
        ),
    ]