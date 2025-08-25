import os
import requests
import json
from langchain_core.tools import tool

@tool
def get_weather_by_location(location: str) -> str:
    """ 
    Return the current weather by a specific location
    
    Args:
        location: place where the user want to know about the weather  
    
    """
    api_key = os.getenv("WEATHERAPI_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    if response.status_code != 200:
        return "The weather could not be obtained."
    
    data = response.json()

    return json.dumps(data)

@tool
def get_weather_forecast(location: str, days: int) -> str:
    """
    Return the weather forecast for the days and location specified by the user
    
    Args:
        location: place where the user want to know about the weather
        days: number of days for the forecast 
    """

    if days not in range(1,4):
        return "Only forecast for 1 to 3 days are allowed."
    
    api_key = os.getenv("WEATHERAPI_KEY")
    url = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={location}&days={days}"
    response = requests.get(url)
    if response.status_code != 200:
        return "The weather forecast could not be obtained."
    
    data = response.json()

    return json.dumps(data)
