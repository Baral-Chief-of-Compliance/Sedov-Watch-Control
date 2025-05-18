from django.db import models


class Institution(models.Model):
    """Учебное заведение"""
    i_name = models.CharField(verbose_name='Наименование Учебного заведения', max_length=256)
    
    def __str__(self):
        return self.i_name
    
    class Meta:
        verbose_name = 'Учебное заведение'
        verbose_name_plural = 'Учебные заведения'