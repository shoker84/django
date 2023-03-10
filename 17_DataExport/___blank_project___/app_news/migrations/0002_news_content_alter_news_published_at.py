# Generated by Django 4.1.4 on 2022-12-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.CharField(blank=True, max_length=5000, verbose_name='Содержимое'),
        ),
        migrations.AlterField(
            model_name='news',
            name='published_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата публикации'),
        ),
    ]
