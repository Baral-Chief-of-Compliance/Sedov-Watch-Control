from django import forms

from watch_control_app.models import Post
from watch_control_app.widgets import TextInputWidget


class PostForm(forms.ModelForm):
    """Форма для добавления и обновления должности пользователя"""
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'p_name': TextInputWidget(
                base_widget=forms.TextInput,
                label='Наименование должности',
                id='p_name'
                ),
            'P_priority': TextInputWidget(
                base_widget=forms.NumberInput,
                label='Приоритет должности',
                id='P_priority'
                ),
        }