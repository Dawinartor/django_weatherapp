import os
from geopy.geocoders import Nominatim
from django.shortcuts import render
from django.views.generic import TemplateView



# Create your views here.

def HomeView(request):
    current_weather = "Sun"
    context = {"current_weather": current_weather}
    return render(request, "weather/home.html", context)

class HomeView(request):
    api_key = os.environ("API_KEY")
    current_weather = 0

    def get_geolocation(self, city_name):
        city = str(city_name)
        geolocator = Nominatim(user_agent="geo_location_app")
        location = geolocator.geocode(city)

        # if location call was successfull extract longitude & latitude
        if location:
            lat, long = location.latitude, location.longitude
            return lat, long
        else:
            print(f"Unable to get geolocation for {city}")
            return None



    def get_weather(self):
        params = {"lat":}
        base_url =  f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"


    #def change_component(self):

class RainView(TemplateView):
    template_name = 'weather/rainning.html'

class SunnyView(TemplateView):
    template_name = 'weather/sunny.html'

class ClearView(TemplateView):
    template_name = 'weather/clear.html'