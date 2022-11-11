from api_config import *
import requests
import json

def get_city_coord(city):
    payload = {'geocode': city,
               'apikey': geo_key,
               'format': 'json'
    }
    r = requests.get('https://geocode-maps.yandex.ru/1.x', params=payload)
    #r.encoding = 'utf-8'
    data = json.loads(r.text)
    try:
        return data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    except:
        return None




def get_weather(city):
    coordinates = get_city_coord(city)
    if coordinates:
        payload = {'lat' : coordinates.split()[1], 'lon' : coordinates.split()[0], 'lang' : 'ru_RU'}
        r = requests.get('https://api.weather.yandex.ru/v2/forecast', params=payload, headers={'X-Yandex-API-Key': weather_key})
        weather_data = json.loads(r.text)
        return weather_data['fact']
    return None

