# Generated by Django 2.1.2 on 2018-10-08 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20181008_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteudo',
            name='corpo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='conteudo',
            name='descricao',
            field=models.TextField(),
        ),
    ]
