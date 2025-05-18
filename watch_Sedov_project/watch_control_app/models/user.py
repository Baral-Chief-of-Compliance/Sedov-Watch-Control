from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from .role import Role
from .post import Post


class User(AbstractBaseUser):
    """Модель пользователя системы"""

    patronymic = models.CharField(verbose_name='Отчество пользователя', max_length=256, blank=True, null=True)
    post = models.ForeignKey(verbose_name='Должность пользователя', to=Post, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.ForeignKey(verbose_name='Роли пользователя', to=Role, on_delete=models.SET_NULL, null=True, blank=True)