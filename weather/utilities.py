# collection of functions for the core functionalities
import os
import requests

# utillity for calling openWeather API and collecting informations
class WeatherCaller:
    def __init__(self):
        # loading API key in system
        self.API_KEY = os.environ.get('API_KEY')
        #self.BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
        self.WEBTHER_FORMAT = {"current_temperature": 0, "temperature_today_max": 0, "temperature_today_min": 0, "uv_today_max": 0, "humidity_today_max": 0}
        # Tempreture converter
        self.temperature_converter = TemperatureConverter()


    def get_url(self, city, country):
        params = {"city": str(city), "country": str(country)}
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={params['city']},{params['country']}&appid={self.API_KEY}"
        return base_url

    def get_weather_data(self, url):
        response = requests.get(str(url))
        return response.json()

    def get_webther_format(self, weather_data):
        webther_data = self.WEBTHER_FORMAT
        webther_data["current_temperature"] = self.temperature_converter(weather_data)
        webther_data["temperature_today_max"] =
        return webther_data


class TemperatureConverter:
    def __init__(self):
        self.KELVIN_CONSTANT = 273.15

    def Kelvin_to_celsius(self, kelvin_value):
        return round(kelvin_value - self.KELVIN_CONSTANT)
