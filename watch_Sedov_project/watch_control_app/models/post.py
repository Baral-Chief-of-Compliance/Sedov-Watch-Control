from django.db import models


class Post(models.Model):
    """Модель должностей пользователей"""

    p_name = models.CharField(verbose_name='Наименование должности пользователя', max_length=256)
    P_priority = models.PositiveIntegerField(verbose_name='Приоритет должности', default=999)

    def __str__(self):
        return self.p_name
    
    class Meta:
        verbose_name = 'Должность пользователя'
        verbose_name_plural = 'Должности пользователей'