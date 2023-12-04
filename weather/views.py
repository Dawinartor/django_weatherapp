from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'weather/home.html'

class RainView(TemplateView):
    template_name = 'weather/rainning.html'

class SunnyView(TemplateView):
    template_name = 'weather/sunny.html'

class ClearView(TemplateView):
    template_name = 'weather/clear.html'