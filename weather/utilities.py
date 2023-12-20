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

    def unix_timestamp_to_europe_time(self, timestamp, timezone_name='Europe/Berlin'):
        target_timezone = pytz.timezone(timezone_name)
        dt_object = datetime.fromtimestamp(timestamp, tz=pytz.utc).astimezone(target_timezone)
        formatted_day_time = dt_object.strftime("%H:%M")  #%Y-%m-%d
        return formatted_day_time


# utillity for calling openWeather API and collecting informations
class WeatherCaller:
    def __init__(self): # todo: add base_url concept
        # loading API key in system
        self.API_KEY = os.environ.get("OpenWeather_API_KEY", "default_value_if_not_set")
        # data converter
        self.data_converter = DataConverter()
        self.WEBTHER_FORMAT = {
            "current_weather_icon": "",
            "current_weather_status": "",
            "current_weather_description": "",
            "date_time_stamp": "",
            "current_temperature": 0,
            "current_temperature_feels_like": 0,
            "today_sunrise": 0,
            "today_sunset": 0,
            "current_uvi": 0,
            "current_wind_speed": 0
        }


    def get_url(self, lat=53.073635, lon=8.806422, exc = ["minutely", "hourly", "daily"]):
        params = {"latitude": lat, "longitude": lon, "excluding_info": ','.join(exc)}
        base_url = (f"https://api.openweathermap.org/data/2.5/onecall?&units=metric" +
                    f"&lat={params['latitude']}" +
                    f"&lon={params['longitude']}" +
                    f"&exclude={params['excluding_info']}" +
                    f"&appid={self.API_KEY}")
        return base_url

    def get_weather_data_raw(self, url):
        response = requests.get(str(url))
        return response.json()

    def data_raw_to_webther_format(self, raw_data):
        webther_data = self.WEBTHER_FORMAT
        webther_data["current_weather_icon"] = raw_data['current']['weather'][0]['icon']
        webther_data["current_weather_status"] = raw_data['current']['weather'][0]['main']  # relevant for ChatGPT later
        webther_data["current_weather_description"] = raw_data['current']['weather'][0]['description']  # relevant for ChatGPT later
        webther_data["date_time_stamp"] = self.data_converter.unix_timestamp_to_europe_time(raw_data["current"]["dt"])
        webther_data["current_temperature"] = raw_data['current']["temp"]  # relevant for ChatGPT later
        webther_data["current_temperature_feels_like"] = raw_data['current']["feels_like"]  # relevant for ChatGPT later
        webther_data["today_sunrise"] = self.data_converter.unix_timestamp_to_europe_time(raw_data['current']["sunrise"])
        webther_data["today_sunset"] = self.data_converter.unix_timestamp_to_europe_time(raw_data['current']["sunset"])
        webther_data["current_uvi"] = raw_data['current']["uvi"]  # relevant for ChatGPT later
        webther_data["current_wind_speed"] = raw_data['current']["wind_speed"]
        return webther_data
