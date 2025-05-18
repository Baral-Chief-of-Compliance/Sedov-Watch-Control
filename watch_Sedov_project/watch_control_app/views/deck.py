from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf.global_settings import LOGIN_URL

from watch_control_app.forms.deck import DeckForm
from watch_control_app.models import Deck
from .tools.tmp_path import TemplatePath
from .tools.success_url import get_success_url


tmp_path = TemplatePath('deck')


class DeckListView(LoginRequiredMixin, ListView):
    """Представление для списка палуб Седова"""
    login_url = LOGIN_URL
    model = Deck
    context_object_name = 'decks'
    template_name = tmp_path.list()


class DeckCreateView(LoginRequiredMixin, CreateView):
    """Представление для добвления палубы в базу"""
    login_url = LOGIN_URL
    model = Deck
    form_class = DeckForm
    template_name = tmp_path.add()
    success_url = get_success_url('deck')


class DeckUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для редактирования Палубы"""
    login_url = LOGIN_URL
    model = Deck
    pk_url_kwarg = 'deck_id'
    context_object_name = 'deck'
    template_name = tmp_path.update()
    form_class = DeckForm
    success_url = get_success_url('deck')


class DeckDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для удаления палубы Седова"""
    login_url = LOGIN_URL
    model = Deck
    pk_url_kwarg = 'deck_id'
    context_object_name = 'deck'
    success_url = get_success_url('deck')

    def get(self, request, *args, **kwargs):
        self.post(self, request, *args, **kwargs)