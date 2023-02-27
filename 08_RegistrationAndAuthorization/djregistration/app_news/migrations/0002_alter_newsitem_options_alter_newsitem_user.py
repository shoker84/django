# Generated by Django 4.1.3 on 2022-12-08 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ['-publicised_at'], 'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='news_user', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь из DJDB'),
        ),
    ]
