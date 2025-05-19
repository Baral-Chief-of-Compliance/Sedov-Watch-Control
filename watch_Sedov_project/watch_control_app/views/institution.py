from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf.global_settings import LOGIN_URL
from django.urls import reverse_lazy

from watch_control_app.forms.institution import InstitutionForm
from watch_control_app.models import Institution
from .tools.tmp_path import TemplatePath
from .tools.success_url import get_success_url


tmp_path = TemplatePath('institution')


class InstitutionListView(LoginRequiredMixin, ListView):
    """Представление для списка институтов членов экипажа"""
    login_url = LOGIN_URL
    model = Institution
    context_object_name = 'institutions'
    template_name = tmp_path.list()


class InstitutionCreateView(LoginRequiredMixin, CreateView):
    """Представление для добавления Института члена экипажа"""
    login_url = LOGIN_URL
    model = Institution
    form_class = InstitutionForm
    template_name = tmp_path.add()
    success_url = reverse_lazy(get_success_url('institution'))


class InstitutionUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для редактирования Института члена экипажа"""
    login_url = LOGIN_URL
    model = Institution
    pk_url_kwarg = 'institution_id'
    context_object_name = 'institution'
    template_name = tmp_path.update()
    form_class=InstitutionForm
    success_url = reverse_lazy(get_success_url('institution'))


class InstitutionDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для удаления Института члена экипажа"""
    login_url = LOGIN_URL
    model = Institution
    pk_url_kwarg = 'institution_id'
    success_url = reverse_lazy(get_success_url('institution'))

    def get(self, request, *args, **kwargs):
        return self.post(*args, **kwargs)