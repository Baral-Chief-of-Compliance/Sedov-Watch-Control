from django.db import models


from .watch import Watch
from .work_time_interval import WorkTimeInterval
from .deck_place import DeckPlace
from .crew_member import CrewMemeber


ABSENCE_REASON : list = [
    ('Др', 'День рождение'),
    ('Бо', 'Болезнь'),
    ('Дг', 'Другое'),
]


class DayWatch(models.Model):
    """День вахты"""
    dw_date = models.DateField(verbose_name="Дата дня вахты")
    dw_watch = models.ForeignKey(verbose_name="вахта", to=Watch, on_delete=models.CASCADE)
    dw_crew_member = models.ForeignKey(verbose_name="Член экипажа", to=CrewMemeber, on_delete=models.CASCADE)
    dw_deck_place = models.ForeignKey(verbose_name="Место на палубе", to=DeckPlace, on_delete=models.SET_NULL, null=True, blank=True)
    dw_time_interval = models.ForeignKey(verbose_name="Смена", to=WorkTimeInterval, on_delete=models.SET_NULL, null=True, blank=True)
    dw_absence = models.BooleanField(verbose_name='Отсутсвие члена экипажа', default=False)
    dw_absence_reason = models.CharField(verbose_name='Причина отсутствия', blank=True, null=True, choices=ABSENCE_REASON, max_length=128)

    def __str__(self):
        return f'день {self.dw_date.strftime("%d.%m.%y")} вахты {self.dw_watch}'
    
    class Meta:
        verbose_name = 'День вахты'
        verbose_name_plural = 'Дни вахты'
