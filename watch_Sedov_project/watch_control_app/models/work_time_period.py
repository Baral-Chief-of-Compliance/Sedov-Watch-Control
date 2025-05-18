import datetime

from django.db import models

from .work_time_interval import WorkTimeInterval


def get_default_work_time_period():
    """Функция для получения конца временного промежутка смены по умолчанию"""
    return datetime.datetime.now() + datetime.timedelta(hours=1)


class WorkTimePeriod(models.Model):
    """Временной промежуток смены"""
    wtp_name = models.CharField(verbose_name='Наименование временного промежутка смены', max_length=256)
    wtp_start_time = models.TimeField(verbose_name='Начала временного промежутка', default=datetime.datetime.now)
    wtp_end_time = models.TimeField(verbose_name='Конец временного промежутка', default=get_default_work_time_period)
    wtp_work_time_interval = models.ManyToManyField(verbose_name='Смены', to=WorkTimeInterval, blank=True)

    def __str__(self):
        return self.wtp_name
    
    class Meta:
        verbose_name='Временной промежуток смены'
        verbose_name_plural='Временные промежутки смены'