# collection of functions for the core functionalities
import os
import requests
import pytz
from datetime import datetime

class DataConverter:
    def __init__(self):
        self.KELVIN_CONSTANT = 273.15

    def Kelvin_to_celsius(self, kelvin_value):
        return round(kelvin_value - self.KELVIN_CONSTANT)

    def unix_timestamp_to_europe(self, timestamp, timezone_name='Europe/Berlin'):
        target_timezone = pytz.timezone(timezone_name)
        dt_object = datetime.fromtimestamp(timestamp, tz=pytz.utc).astimezone(target_timezone)
        formatted_day_time = dt_object.strftime("%H:%M:%S %Z")  #%Y-%m-%d
        return formatted_day_time


# utillity for calling openWeather API and collecting informations
class WeatherCaller:
    def __init__(self): # todo: add base_url concept
        # loading API key in system
        self.API_KEY = os.environ.get('API_KEY')
        # data converter
        self.data_converter = DataConverter()
        self.WEBTHER_FORMAT = {
            "current_weather_status": "",
            "current_temperature": 0,
            "temperature_today_max": 0,
            "temperature_today_min": 0,
            "sunrise_today": 0,
            "sunset_today": 0
        }


    def get_url(self, city, country):
        params = {"city": str(city), "country": str(country)}
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={params['city']},{params['country']}&appid={self.API_KEY}"
        return base_url

    def get_weather_data_raw(self, url):
        response = requests.get(str(url))
        return response.json()

    def get_webther_format(self, weather_data):
        webther_data = self.WEBTHER_FORMAT
        webther_data["current_weather_status"] = weather_data["weather"][0]["main"]
        webther_data["current_temperature"] = self.data_converter.Kelvin_to_celsius(weather_data["main"]["temp"])
        webther_data["temperature_today_max"] = self.data_converter.Kelvin_to_celsius(weather_data["main"]["temp_max"])
        webther_data["temperature_today_min"] = self.data_converter.Kelvin_to_celsius(weather_data["main"]["temp_min"])
        webther_data["sunrise_today"] = self.data_converter.unix_timestamp_to_europe(weather_data["sys"]["sunrise"])
        webther_data["sunset_today"] = self.data_converter.unix_timestamp_to_europe(weather_data["sys"]["sunset"])
        return webther_data
