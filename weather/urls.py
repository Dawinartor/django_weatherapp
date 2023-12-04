from django.urls import path
from . import views

urlpattern = [
    path('', views.HomeView.as_view(), name='home'),
]
