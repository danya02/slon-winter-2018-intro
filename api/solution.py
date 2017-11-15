#!/usr/bin/python3
import requests
import math
import sys


def get_weather_for_city_at_point(lat: float, lon: float, api_key: str) -> dict:
    """
    Get a weather object at a point.
    A weather object is a dict.
    An example of what this may contain is at:
    http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1
    """
    with requests.get(
            "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&APPID={}".format(lat, lon,
                                                                                           api_key)) as r:
        return r.json()


def get_weather_for_cities_around_point(lat: float, lon: float, api_key: str, count: int = 10) -> [dict]:
    """
    Get a list of weather objects around a point.
    Each weather object is a dict.
    An example of what this may contain is at:
    http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1
    """
    with requests.get(
            "http://api.openweathermap.org/data/2.5/find?lat={}&lon={}&cnt={}&APPID={}".format(lat, lon, count,
                                                                                               api_key)) as r:
        return r.json()['list']


def get_coords_of_object(name: str, api_key: str = None) -> (float, float):
    """
    Get coords for the object given, as (lat, lon).
    Example of valid object description: "Москва, Тверская улица, дом 7".
    Uses Yandex's geocoder.
    Optional api_key (the free Yandex.Maps API key) needed if geocoding objects outside of Yandex's target area
    (Russia and surrounding countries).
    """
    name = name.translate({ord(' '): '+'})
    with requests.get("https://geocode-maps.yandex.ru/1.x/?geocode={}&format=json".format(
            name) if api_key is None else "https://geocode-maps.yandex.ru/1.x/?geocode={}&key={}&format=json".format(
        name, api_key)) as r:
        root = r.json()
        lon, lat = root['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        lon = float(lon)
        lat = float(lat)
        return lat, lon


def get_canonical_name_of_object(name: str, api_key: str = None) -> str:
    """
    Get the canonical name of a given object.
    Example of valid object description: "Москва, Тверская улица, дом 7".
    Uses Yandex's geocoder.
    Optional api_key (the free Yandex.Maps API key) needed if geocoding objects outside of Yandex's target area
    (Russia and surrounding countries).
    """
    name = name.translate({ord(' '): '+'})
    with requests.get("https://geocode-maps.yandex.ru/1.x/?geocode={}&format=json".format(
            name) if api_key is None else "https://geocode-maps.yandex.ru/1.x/?geocode={}&key={}&format=json".format(
        name, api_key)) as r:
        return r.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
            'GeocoderMetaData']['text']


def is_precipitating(weather: dict,
                     conditions: tuple = (
                             200, 201, 202, 210, 211, 212, 221, 230, 231, 232, 300, 301, 302, 310, 311,
                             312, 313, 314, 321, 500, 501, 502, 503, 504, 511, 520, 521, 522, 531, 600,
                             601, 602, 611, 612, 615, 620, 621, 622)) -> bool:
    """
    Return True if there is precipitation in the weather object provided.
    What is defined as precipitation is given in the optional conditions param.
    """
    return weather['weather'][0]['id'] in conditions


def get_distance(weather1: dict, weather2: dict, radius: float = 6371.0) -> float:
    """
    Given two weather dicts, get the distance between them, in kilometers.
    Uses equirectangular approximation. Assumes sphere; error up to 0.5% expected.
    If sphere in question is not Earth, an optional radius param is the radius of the sphere, in expected output units.
    """

    lat1 = weather1['coord']['lat']
    lat2 = weather2['coord']['lat']
    lon1 = weather1['coord']['lon']
    lon2 = weather2['coord']['lon']
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    lon1 = math.radians(lon1)
    lon2 = math.radians(lon2)
    x = (lon2 - lon1) * math.cos(0.5 * (lat2 + lat1))
    y = lat2 - lat1
    return radius * math.sqrt(x * x + y * y)


def get_closest_city_that_passes_test(lat: float, lon: float, api_key: str, test=is_precipitating,
                                      negate: bool = True, accept_self: bool = False) -> (dict, float):
    """
    Get a closest city that passes a given test around a point.
    Return the weather dict and the distance to it in kilometers.
    The test can be optionally negated.
    If accept_self is true, the given city will be returned, if it passes the test.
    """
    this_city = get_weather_for_city_at_point(lat, lon, api_key)
    if (not test(this_city) if negate else test(this_city)) and accept_self:
        return (this_city,0)
    list_of_cities = get_weather_for_cities_around_point(lat, lon, api_key, 50)
    closest = None
    closest_distance = 32768.0
    for i in list_of_cities:
        try:
            if get_distance(this_city, i) < closest_distance and (not test(i) if negate else test(i)):
                closest_distance = get_distance(this_city, i)
                closest = i
        except:
            pass
    return closest, closest_distance


def turn_weather_object_into_canonical_name(weather: dict) -> str:

    return get_canonical_name_of_object(weather['name'])


if __name__ == '__main__':
    api_key="2e5139acb91332898b675f24f8941790" # change this to your key
    if len(sys.argv)==1:
        print('No command-line argument, defaulting to "Moscow". Select your own input as first argument after name.')
        input_name="Moscow"
    else:
        input_name = sys.argv[1]
    lat,lon = get_coords_of_object(input_name)
    result = get_closest_city_that_passes_test(lat,lon, api_key, accept_self=True)
    print(turn_weather_object_into_canonical_name(result[0]))
