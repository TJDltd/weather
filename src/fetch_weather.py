from config import WeatherDataConfig
import requests

CURRENT_URL = WeatherDataConfig.CURRENT_WEATHER_URL

def fetch_current_weather(location: str) -> dict:
    return_object = requests.get(f"{CURRENT_URL}{location}&current=temperature_2m")
    print(CURRENT_URL)
    return return_object.json()
