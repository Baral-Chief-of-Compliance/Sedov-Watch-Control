from django.db import models


class Deck(models.Model):
    """Палуба Седова"""
    d_name = models.CharField(verbose_name='Наименования палубы', max_length=256)
    d_prioriter = models.PositiveIntegerField(verbose_name='Приоритет палубы', default=999)
    d_svg = models.FileField(verbose_name='SVG судная', upload_to='decks/')

    def __str__(self):
        return self.d_name
    
    class Meta:
        verbose_name = 'Палуба Седова'
        verbose_name_plural = 'Палубы Седова'
        ordering = ['d_prioriter']