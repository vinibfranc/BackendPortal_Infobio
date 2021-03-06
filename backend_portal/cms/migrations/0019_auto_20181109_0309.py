# Generated by Django 2.1.2 on 2018-11-09 03:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0018_auto_20181108_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opportunity',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Moderado'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='area',
            field=models.CharField(max_length=150, verbose_name='área'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='city',
            field=models.CharField(max_length=100, verbose_name='cidade'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='description',
            field=models.TextField(verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='institution',
            field=models.CharField(max_length=150, verbose_name='instituição'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='title',
            field=models.CharField(max_length=150, verbose_name='título'),
        ),
    ]
