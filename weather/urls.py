from django.urls import path
from .views import handle_geolocation
from . import views

urlpatterns = [
    path('', views.WebtherView, name='home'),
    path('default', views.defaultView.as_view(), name='default'),
    path('handle_geolocation/', handle_geolocation, name='handle_geolocation'),
]
