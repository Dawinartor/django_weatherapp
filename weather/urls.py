from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('rain', views.RainView.as_view(), name='rain'),
    path('sun', views.SunnyView.as_view(), name='sun'),
    path('clear', views.ClearView.as_view(), name='clear'),
]
