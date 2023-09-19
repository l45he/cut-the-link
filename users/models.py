from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class URLs(models.Model):
    max_link_length = 400

    username = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Имя пользователя',
        blank=True
    )
    name = models.CharField(
        'Ссылка',
        max_length=max_link_length,
        help_text=f'Максимальная длина ссылки - {max_link_length} символов'
    )
    short_name = models.SlugField(
        'Сокращенная ссылка',
        max_length=50,
        unique=True,
        error_messages=
        {
            'unique': 'Такая ссылка уже существует'
        }
    )

    #правильное отображение названий в соответствии с полем name
    def __str__(self):
        return self.short_name

    #указываем правильные названия таблицы на русском и в разных числах
    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'