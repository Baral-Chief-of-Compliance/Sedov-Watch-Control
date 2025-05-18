import datetime

from django.db import models


def default_end_date() -> datetime.date:
    """Метод по созданию даты конца вахты по умолчанию"""
    return datetime.date.today + datetime.timedelta(days=30)


class Watch(models.Model):
    """Модель вахты"""
    w_start_date = models.DateField(verbose_name='Дата начала вахты', default=datetime.date.today)
    w_end_date = models.DateField(verbose_name='Дата конца вахты', default=default_end_date)

    def __str__(self):
        return f'вахта с {self.w_start_date.strftime("%d.%m.%y")} по {self.w_end_date.strftime("%d.%m.%y")}'
    
    class Meta:
        verbose_name='Вахта'
        verbose_name_plural='Вахты'