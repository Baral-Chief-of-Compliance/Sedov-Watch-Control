from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf.global_settings import LOGIN_URL

from watch_control_app.forms.crew_memeber import CrewMemberForm
from watch_control_app.models import CrewMemeber
from .tools.tmp_path import TemplatePath
from .tools.success_url import get_success_url


tmp_path = TemplatePath('crew_members')


class CrewMemberListView(LoginRequiredMixin, ListView):
    """Представление для списка членов экипажа"""
    login_url = LOGIN_URL
    model = CrewMemeber
    context_object_name = 'crew_members'
    template_name = tmp_path.list()


class CrewMemeberCreateView(LoginRequiredMixin, CreateView):
    """Представление для добавления члена экипажа"""
    login_url = LOGIN_URL
    model = CrewMemeber
    form_class = CrewMemberForm
    template_name = tmp_path.add()
    success_url = get_success_url('crew_members')


class CrewMemberUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для обновления информации о члене экипажа"""
    login_url = LOGIN_URL
    model = CrewMemeber
    pk_url_kwarg = 'crew_member_id'
    template_name = tmp_path.update()
    context_object_name = 'crew_member'
    form_class=CrewMemberForm
    success_url = get_success_url('crew_members')


class CrewMemberDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для удаления члена экипажа"""
    login_url = LOGIN_URL
    model = CrewMemeber
    pk_url_kwarg = 'crew_member_id'
    context_object_name = 'crew_member'
    success_url = get_success_url('crew_members')

    def get(self, request, *args, **kwargs):
        self.post(self, request, *args, **kwargs)