# Generated by Django 2.1.2 on 2018-10-09 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20181008_2127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='conteudo',
            options={'ordering': ['data_criacao']},
        ),
    ]