from django import forms

from watch_control_app.models import CrewMemeber


class CrewMemberForm(forms.ModelForm):
    """Форма для добавления и обновления члена экипажа"""
    class Meta:
        model = CrewMemeber
        fields = '__all__'