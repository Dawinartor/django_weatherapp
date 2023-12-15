from django.urls import path
from .views import handle_geolocation
from . import views

urlpatterns = [
    path('', views.WebtherView, name='home'),
    path('handle_geolocation/', handle_geolocation, name='handle_geolocation'),
]
