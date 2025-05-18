from django.db import models

from .deck import Deck


class DeckPlace(models.Model):
    """Место на палубе"""
    dp_name = models.CharField(verbose_name='Наименование места на палубе', max_length=256)
    dp_description = models.TextField(verbose_name='Описание палубы', blank=True, null=True)
    dp_svg_name = models.CharField(verbose_name='Наименование места в SVG файле', max_length=256)
    dp_svg_id = models.CharField(verbose_name='Id места в SVG файле', max_length=256)
    dp_deck = models.ForeignKey(verbose_name='Палуба', to=Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.dp_name
    
    class Meta:
        verbose_name='Место на палубе'
        verbose_name_plural='Места на палубе'
    