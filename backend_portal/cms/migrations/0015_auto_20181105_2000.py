# Generated by Django 2.1.2 on 2018-11-05 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20181105_1958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='id_section',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='content',
            name='id_category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
