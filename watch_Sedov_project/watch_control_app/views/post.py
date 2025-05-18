from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf.global_settings import LOGIN_URL

from watch_control_app.forms.post import PostForm
from watch_control_app.models import Post
from .tools.tmp_path import TemplatePath
from .tools.success_url import get_success_url


tmp_path = TemplatePath('post')


class PostListView(LoginRequiredMixin, ListView):
    """Представление для списка должностей членов экипажа"""
    login_url = LOGIN_URL
    model = Post
    context_object_name = 'posts'
    template_name = tmp_path.list()


class PostCreateView(LoginRequiredMixin, CreateView):
    """Представление для добавления должности члена экипажа"""
    login_url = LOGIN_URL
    model = Post
    form_class = PostForm
    template_name = tmp_path.add()
    success_url = get_success_url('post')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    """Представление для обновления должности члена экипажа"""
    login_url = LOGIN_URL
    model = Post
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    template_name = tmp_path.update()
    from_class=PostForm
    success_url = get_success_url('post')


class PostDeleteView(LoginRequiredMixin, DeleteView):
    """Представление для удаления Должности члена экипажа"""
    login_url = LOGIN_URL
    model = Post
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'
    success_url = get_success_url('post')

    def get(self, request, *args, **kwargs):
        self.post(self, request, *args, **kwargs)