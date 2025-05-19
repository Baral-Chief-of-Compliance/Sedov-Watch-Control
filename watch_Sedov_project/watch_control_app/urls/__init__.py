from django.urls import path, include

app_name = 'watch_control_app'

urlpatterns = [
    path('', include('watch_control_app.urls.index')),
    path('post/', include('watch_control_app.urls.post')),
    path('crew_members/', include('watch_control_app.urls.crew_members')),
    path('institutions/', include('watch_control_app.urls.institution')),
    path('deck/', include('watch_control_app.urls.deck')),
]
