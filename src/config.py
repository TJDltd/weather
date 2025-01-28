import os
import dotenv

dotenv.load_dotenv('/Users/tomdavey/repos/weather/.env')
KEY = os.getenv("API_KEY")

class WeatherDataConfig:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"
    CURRENT_WEATHER_URL = f"{BASE_URL}/"
