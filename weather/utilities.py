# collection of functions for the core functionalities
import os
import requests
from geopy.geocoders import Nominatim

# utillity for calling openWeather API and collecting informations
class WeatherCaller:
    def __init__(self):
        # loading API key in system
        self.API_KEY = os.environ.get('API_KEY')

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


    def get_url(self, lat, lon, exc=[]):
        params = {"lattitude": lat, "longitude": lon, "exclude": exc}
        base_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={params['lattitude']}&lon={params['longitude']}&exclude={','.join(params['exclude'])}&appid={self.API_KEY}"
        return base_url

    def get_weather_data(self, url):
        response = requests.get(str(url))
        return response.json()