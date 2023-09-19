# Generated by Django 4.2.5 on 2023-09-17 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='short_name',
            field=models.SlugField(verbose_name='Сокращенная ссылка'),
        ),
        migrations.AlterField(
            model_name='urls',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Имя пользователя'),
        ),
    ]
