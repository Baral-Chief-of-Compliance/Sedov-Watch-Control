from django.db import models


class WorkTimeInterval(models.Model):
    """Смена"""
    wti_name = models.CharField(verbose_name='Наименование смены', max_length=256)
    wti_prioritet = models.PositiveIntegerField(verbose_name='Приоритет смены', default=999)

    def __str__(self):
        return self.wti_name
    
    class Meta:
        verbose_name='Смена на вахте'
        verbose_name_plural='Смены на вахте'