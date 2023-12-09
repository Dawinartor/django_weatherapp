from django.shortcuts import render
from django.views.generic import TemplateView
from .utilities import WeatherCaller


# Create your views here.

weather_util = WeatherCaller()
base_url = weather_util.get_url("Bremen", "") #TODO: country is optional
print(base_url)
weather_data = weather_util.get_weather_data(base_url)
print(weather_data)
ret = weather_util.get_webther_format(weather_data)
print(ret)

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