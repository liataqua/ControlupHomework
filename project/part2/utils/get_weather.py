import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_KEY = os.getenv("API_KEY")
URL = os.getenv("BASE_API")

# q = US zipcode, UK postcode, city name, IP, etc.
@staticmethod
def get_current_weather(q_param):
    endpoint = f"{URL}/current.json"
    params = {"key": API_KEY, "q": q_param}
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()["current"]["temp_f"]