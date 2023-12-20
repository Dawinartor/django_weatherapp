from django.urls import path
from .views import DefaultView, WebtherView, handle_geolocation

urlpatterns = [
    # URL pattern for the DefaultView
    path('', DefaultView.as_view(), name='default'),

    # URL pattern for the WebtherView
    path('webther/<latitude>/<longitude>/', WebtherView.as_view(), name='webther'),

    # URL pattern for the handle_geolocation view
    path('handle_geolocation/', handle_geolocation, name='handle_geolocation'),
]
