from django import forms

from watch_control_app.models.institution import Institution
from watch_control_app.widgets import TextInputWidget


class InstitutionForm(forms.ModelForm):
    """Форма для добавления и обновления института члена экипажа"""

    class Meta:
        fields = '__all__'
        model = Institution
        widgets = {
            'i_name': TextInputWidget(
                base_widget=forms.TextInput,
                label='Наименование учебного заведения',
                id='i_name'
                )
        }
