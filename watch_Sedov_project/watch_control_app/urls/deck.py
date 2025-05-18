from django.urls import path

from .tools.url_path import UrlPath
from watch_control_app.views.deck import DeckListView, DeckCreateView, DeckDeleteView, DeckUpdateView


url_path = UrlPath('deck')


urlpatterns = [
    path('list/', view=DeckListView.as_view(), name=url_path.list()),
    path('add/', view=DeckCreateView.as_view(), name=url_path.add()),
    path('update/<int:deck_id>/', view=DeckUpdateView.as_view(), name=url_path.update()),
    path('delete/<int:deck_id>/', view=DeckDeleteView.as_view(), name=url_path.delete())
]
