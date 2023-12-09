from django.urls import path
from . import views

urlpatterns = [
    path('', views.WebtherView.as_view(), name='home'),
]
