from django.db import models


class Role(models.Model):
    """Модель роли пользователя"""
    r_name = models.CharField(verbose_name='Наименование роли пользователя', max_length=256)

    def __str__(self):
        return self.r_name
    
    class Meta:
        verbose_name = 'Роль пользователя'
        verbose_name_plural = 'Роли пользователей'