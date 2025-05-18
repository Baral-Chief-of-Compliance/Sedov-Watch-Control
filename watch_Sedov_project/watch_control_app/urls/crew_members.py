from django.urls import path

from watch_control_app.views.crew_member import CrewMemberListView, CrewMemberDeleteView, CrewMemberUpdateView, CrewMemeberCreateView
from .tools.url_path import UrlPath


url_path = UrlPath('crew_members')

urlpatterns = [
    path('list/', view=CrewMemberListView.as_view(), name=url_path.list()),
    path('add/', view=CrewMemeberCreateView.as_view(), name=url_path.add()),
    path('update/<int:crew_member_id>/', view=CrewMemberUpdateView.as_view(), name=url_path.update()),
    path('delete/<int:crew_member_id>/', view=CrewMemberDeleteView.as_view(), name=url_path.delete())
]
