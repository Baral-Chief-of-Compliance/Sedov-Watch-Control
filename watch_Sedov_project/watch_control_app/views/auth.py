from django.contrib.auth.views import LoginView

from watch_control_app.forms.auth import AuthenticationForm


class AuthFormView(LoginView):
    """Представления авторизации"""
    authentication_form = AuthenticationForm
    template_name = 'login.html'
    next_page='watch_control_app:index'