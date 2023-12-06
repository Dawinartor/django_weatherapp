from django.shortcuts import render
from django.views.generic import TemplateView




# Create your views here.

def HomeView(request):
    current_weather = "Sun"
    context = {"current_weather": current_weather}
    return render(request, "weather/home.html", context)

class RainView(TemplateView):
    template_name = 'weather/rainning.html'

class SunnyView(TemplateView):
    template_name = 'weather/sunny.html'

class ClearView(TemplateView):
    template_name = 'weather/clear.html'