from django import forms

from watch_control_app.models.deck import Deck
from watch_control_app.widgets import TextInputWidget


class DeckForm(forms.ModelForm):
    """Форма для добавления и редактирования Палубы"""
    class Meta:
        fields = '__all__'
        model = Deck
        widgets = {
            'd_name': TextInputWidget(
                base_widget=forms.TextInput,
                label='Наименование палубы',
                id='d_name'
            ),
            'd_prioriter' : TextInputWidget(
                base_widget=forms.NumberInput,
                label='Приоритет палубы',
                id='d_prioriter'
            ),
            'd_svg': TextInputWidget(
                base_widget=forms.FileInput,
                label='sVG палубы',
                id='d_svg'
            )
        }