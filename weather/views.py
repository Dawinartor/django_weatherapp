from django.shortcuts import render
# from django.views.generic import TemplateView
from .utilities import WeatherCaller

# Current TODi: Create various components for all weather conditions
# List: Thunderstorm, Drizzle, Rain, Snow, Atmosphere, Clear, Clouds

# Create your views here.
def WebtherView(request):
    weather_templates = {
        'thunderstorm': 'weather/thunderstorm.html',
        'drizzle': 'weather/drizzle.html',
        'rain': 'weather/rain.html',
        'snow': 'weather/snow.html',
        'atmosphere': 'weather/atmosphere.html',
        'clear': 'weather/clear.html',
        'clouds': 'weather/clouds.html',
        'sunny': 'weather/sun.html',  # unused template so far
    }
    template_name = ""

    weather_util = WeatherCaller()
    base_url = weather_util.get_url("Bremen", "Germany")
    raw_data = weather_util.get_weather_data_raw(base_url)
    context = weather_util.get_webther_format(raw_data)
    print(context)
    context['current_weather_status'] = "Sun"

    # conditional template switch logic
    if context['current_weather_status'] == "Thunderstorm":
        template_name = weather_templates['thunderstorm']
    elif context['current_weather_status'] == "Drizzle":
        template_name = weather_templates['drizzle']
    elif context['current_weather_status'] == "Rain":
        template_name = weather_templates['rain']
    elif context['current_weather_status'] == "Snow":
        template_name = weather_templates['snow']
    elif context['current_weather_status'] == "Atmosphere":
        template_name = weather_templates['atmosphere']
    elif context['current_weather_status'] == "Clear":
        template_name = weather_templates['clear']
    elif context['current_weather_status'] == "Clouds":
        template_name = weather_templates['clouds']
    elif context['current_weather_status'] == "Sun":
        template_name = weather_templates['sunny']

    return render(request, template_name, context)

#def WebtherView(TemplateView): #TODOO: implement api call and showing data in view


