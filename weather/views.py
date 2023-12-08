from django.shortcuts import render
from django.views.generic import TemplateView
from .utilities import WeatherCaller


# Create your views here.

weather_util = WeatherCaller()
print(weather_util.get_geolocation("Bremen"))
lat, lon = weather_util.get_geolocation("Bremen")
base_url = weather_util.get_url(lat, lon, ["minutely", "hourly", "daily", "alerts"])
print(base_url)
weather_data = weather_util.get_weather_data(base_url)
print(weather_data)

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