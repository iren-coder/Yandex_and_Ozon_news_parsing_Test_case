# Generated by Django 4.1 on 2022-09-02 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_parser', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OzonNews',
        ),
        migrations.DeleteModel(
            name='YandexNews',
        ),
    ]
