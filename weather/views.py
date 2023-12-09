from django.shortcuts import render
from django.views.generic import TemplateView
from .utilities import WeatherCaller


# Create your views here.
def WebtherView(request):
    weather_templates = {
        'rainny': 'weather/rainning.html',
        'sunny': 'weather/sunny.html',
        'clear': 'weather/clear.html'
    }
    template_name = ""

    weather_util = WeatherCaller()
    base_url = weather_util.get_url("Bremen", "Germany")
    raw_data = weather_util.get_weather_data_raw(base_url)
    context = weather_util.get_webther_format(raw_data)

    # conditional template switch logic
    if context['current_weather_status'] == "Drizzel" or "Rain" or "Thunderstorm" or "Snow":
        template_name = weather_templates['rainny']
    if context['current_weather_status'] == "Sun":
        template_name = weather_templates['sunny']
        print(template_name)
    if context['current_weather_status'] == "Clear":
        template_name = weather_templates['clear']



    return render(request, template_name, context)

#def WebtherView(TemplateView): #todo: implement api call and showing data in view
 #   template_name = 'base.html'

  #  weather_templates = {
   #     'rainny': 'weather/rain.html',
    #    'sunny': 'weather/sun.html',
     #   'clear': 'weather/clear.html'
   # }


