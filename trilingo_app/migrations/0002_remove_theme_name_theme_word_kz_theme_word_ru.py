# Generated by Django 5.0.2 on 2024-02-21 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trilingo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='name',
        ),
        migrations.AddField(
            model_name='theme',
            name='word_kz',
            field=models.CharField(default='', max_length=35, verbose_name='Название темы на казахском'),
        ),
        migrations.AddField(
            model_name='theme',
            name='word_ru',
            field=models.CharField(default='', max_length=35, verbose_name='Название темы на английском'),
        ),
    ]
