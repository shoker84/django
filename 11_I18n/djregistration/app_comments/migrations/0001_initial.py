# Generated by Django 4.1.3 on 2022-12-08 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_news', '0002_alter_newsitem_options_alter_newsitem_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('news', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_news_item', to='app_news.newsitem', verbose_name='Новость')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь из DJDB')),
            ],
            options={
                'verbose_name': 'комментарий',
                'verbose_name_plural': 'комментарии',
                'db_table': 'commentaries',
                'ordering': ['-create_at'],
            },
        ),
    ]
