from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from .utilities import WeatherCaller
import json

class DefaultView(TemplateView):
    template_name = 'weather/default.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if it's a POST request and if latitude and longitude are provided
        if request.method == 'POST':
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            if latitude is not None and longitude is not None:
                # If latitude and longitude are provided, redirect to WebtherView
                return redirect('webther', latitude=latitude, longitude=longitude)

        # If it's not a POST request or if latitude and longitude are not provided, render default view
        return super().dispatch(request, *args, **kwargs)

class WebtherView(TemplateView):
    template_name = ''  # Default template

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            data = json.loads(request.body)
            latitude = data.get('latitude')
            longitude = data.get('longitude')

            # Process the latitude and longitude as needed
            weather_util = WeatherCaller()
            base_url = weather_util.get_url(latitude, longitude)
            raw_data = weather_util.get_weather_data_raw(base_url)
            context = weather_util.data_raw_to_webther_format(raw_data)
            print(context)

            # conditional template switch logic
            if context['current_weather_status'] == "Thunderstorm":
                self.template_name = 'weather/thunderstorm.html'
            elif context['current_weather_status'] == "Drizzle":
                self.template_name = 'weather/drizzle.html'
            elif context['current_weather_status'] == "Rain":
                self.template_name = 'weather/rain.html'
            elif context['current_weather_status'] == "Snow":
                self.template_name = 'weather/snow.html'
            elif context['current_weather_status'] == "Atmosphere":
                self.template_name = 'weather/atmosphere.html'
            elif context['current_weather_status'] == "Clear":
                self.template_name = 'weather/clear.html'
            elif context['current_weather_status'] == "Clouds":
                self.template_name = 'weather/clouds.html'
            elif context['current_weather_status'] == "Sun":
                self.template_name = 'weather/sun.html'

        return super().dispatch(request, *args, **kwargs)

@csrf_exempt
def handle_geolocation(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        # Process the latitude and longitude as needed
        # For example, you can save them to a database or perform other actions
        variable = process_geolocation(latitude, longitude)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def process_geolocation(latitude, longitude):
    # Access latitude and longitude in this function
    # Process the data as needed
    print(f"Received latitude: {latitude} & longitude: {longitude}")
    geo_coordinates = {"latitude": latitude, "longitude": longitude}
    return geo_coordinates
