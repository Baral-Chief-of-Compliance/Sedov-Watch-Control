from django.urls import path

from .tools.url_path import UrlPath
from watch_control_app.views.institution import InstitutionListView, InstitutionCreateView, InstitutionDeleteView, InstitutionUpdateView


url_path = UrlPath('institution')


urlpatterns = [
    path('list/', view=InstitutionListView.as_view(), name=url_path.list()),
    path('add/', view=InstitutionCreateView.as_view(), name=url_path.add()),
    path('update/<int:institution_id>/', view=InstitutionUpdateView.as_view(), name=url_path.update()),
    path('delete/<int:institution_id>/', view=InstitutionDeleteView.as_view(), name=url_path.delete())
]
