# Generated by Django 2.1.2 on 2018-10-09 19:37

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20181009_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='body',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
