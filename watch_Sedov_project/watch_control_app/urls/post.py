from django.urls import path

from .tools.url_path import UrlPath
from watch_control_app.views.post import PostListView, PostCreateView, PostUpdateView, PostDeleteView


url_path = UrlPath('post')


urlpatterns = [
    path('list/', view=PostListView.as_view(), name=url_path.list()),
    path('add/', view=PostCreateView.as_view(), name=url_path.add()),
    path('update/<int:post_id>/', view=PostUpdateView.as_view(), name=url_path.update()),
    path('delete/<int:post_id>/', view=PostDeleteView.as_view(), name=url_path.delete())
]
