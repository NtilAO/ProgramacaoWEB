import requests
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def tempoHojeLisboa(request):
    weather_url = 'https://api.ipma.pt/public-data/forecast/meteorology/cities/daily/1110600.json'
    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        today_forecast = next((item for item in weather_data if item['forecastDate'] == datetime.today().strftime('%Y-%m-%d')), None)

        # Endpoint para obter as classes de tempo
        weather_classes_url = 'https://api.ipma.pt/public-data/weather-type-classes.json'
        response_classes = requests.get(weather_classes_url)
        if response_classes.status_code == 200:
            weather_classes = response_classes.json()
            weather_description = next((item['descIdWeatherTypePT'] for item in weather_classes if item['idWeatherType'] == today_forecast['idWeatherType']), "Descrição não disponível")

            icon_filename = f"{today_forecast['idWeatherType']}.svg"

            context = {
                'city': 'Lisboa',
                'min_temp': today_forecast['tMin'],
                'max_temp': today_forecast['tMax'],
                'date': today_forecast['forecastDate'],
                'weather_description': weather_description,
                'icon_url': f"meteo/{icon_filename}"
            }

            return render(request, 'meteo/weather_lisbon.html', context)
        else:
            return render(request, 'meteo/weather_lisbon.html', {'error': 'Erro ao obter descrições das classes de tempo.'})
    else:
        return render(request, 'meteo/weather_lisbon.html', {'error': 'Erro ao obter previsão do tempo.'})
