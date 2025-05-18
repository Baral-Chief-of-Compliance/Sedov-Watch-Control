from django import forms

from watch_control_app.models import Post


class PostForm(forms.ModelForm):
    """Форма для добавления и обновления должности пользователя"""
    class Meta:
        model = Post
        fields = '__all__'