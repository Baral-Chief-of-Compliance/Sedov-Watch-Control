from django.db import models

from .post import Post
from .institution import Institution


SEX : list = [
    ('M', 'Мужчина'),
    ('W','Женщина')
]


class CrewMemeber(models.Model):
    """
    Модель члена экипажа Седова, обычно это струденты,
    которые имеют разные должности, касаемо выхты
    """
    cm_name = models.CharField(verbose_name='Имя члена экипажа', max_length=256)
    cm_surname = models.CharField(verbose_name='Фамилия члена экипажа', max_length=256)
    cm_patronymic = models.CharField(verbose_name='Отчество члена экипажа', max_length=256, blank=True, null=True)
    cm_course = models.PositiveSmallIntegerField(verbose_name='Курс члена экипажа', blank=True, null=True)
    cm_birthday = models.DateField(verbose_name='День рождения члена экипажа')
    cm_status = models.BooleanField(verbose_name='Активен', default=True)
    cm_post = models.ForeignKey(verbose_name='Должность члена экипажа', to=Post, on_delete=models.SET_NULL, null=True, blank=True)
    cm_sex = models.CharField(verbose_name='Пол члена экипажа', choices=SEX, max_length=128)
    cm_institution = models.ForeignKey(verbose_name='Учебное заведение члена экипажа', to=Institution, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.cm_surname} {self.cm_name} {self.cm_patronymic}'
    
    class Meta:
        verbose_name = 'Член экипажа'
        verbose_name_plural = 'Члены экипажа'