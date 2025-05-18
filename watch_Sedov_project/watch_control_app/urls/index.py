from django.urls import path
from django.contrib.auth.views import LogoutView

from watch_control_app.views.index import index
from watch_control_app.views.auth import AuthFormView


urlpatterns = [
    path('', view=index, name='index'),
    path('login/', view=AuthFormView.as_view(), name='login'),
    path('logout/', view=LogoutView.as_view(), name='logout'),
]
