"""
Important metrics in the weather API:
    standard: Kelvin (default)
    metric: Celsius (this is used frequently)
    imperial: Fahrenheit
"""

"""
Openweather API recommends to get weather conditions using geographical coordinates.
So first we use Geocoding API to get the coordinates and then use those coordinates to get the 
weather conditions.

Gecoding API: Map places to coordinates

This is an example reference for the above API;
A sample JSON response from the geocoding API:
[
  {
    "name": "Hyderabad",
    "lat": 17.384,
    "lon": 78.4564,
    "country": "IN"
  }
]

The main parameters should be:
    q --> city name
    appid --> api key
    limit --> You give a number. There might be various locations with the same name.
              Setting a limit would cap the results to the most prominent ones.

geo_api_url = "http://api.openweathermap.org/geo/1.0/direct"
weather_url = "https://api.openweathermap.org/data/2.5/weather"

Now we reconstruct the url:
    total_url = weather_url + "?" + "appid=" + "api_key" + "&q=" + city
    The things which are after the '?' are called parameters and they are seperated by '&'.
"""
import requests
import os # This module is used to access environment variables
from dotenv import load_dotenv # This module is used to load environment variables
import logging
import json

logging.basicConfig(
    filename="Week6\Openweather\openweather_api.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

load_dotenv() # This will load the environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise ValueError("API key not found. Check your .env file.")

city = input("Enter the city name to get weather info: ")
geo_url = "http://api.openweathermap.org/geo/1.0/direct"

geo_params = {
    "q": city,
    "limit": 1,
    "appid": API_KEY
}

# geo_response will be a python dictionary as we used .json() at the end
geo_response = requests.get(geo_url, params=geo_params).json()

lat = geo_response[0]["lat"]
lon = geo_response[0]["lon"]

if not geo_response:
    print("City not found. Please try again.")
    exit()

weather_url = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
    "units": "metric"
}

weather_response = requests.get(weather_url, params=weather_params)
weather_response.raise_for_status()
weather_data = weather_response.json()

weather_info = {
    "City": weather_data['name'],
    "Temperature": f"{weather_data['main']['temp']}°C",
    "Humidity": f"{weather_data['main']['humidity']}%",
    "Condition": f"{weather_data['weather'][0]['description'].title()}",
    "Wind Speed": f"{weather_data['wind']['speed']} m/s"
}

file_path = "Week6\Openweather\weather_log.json"

try:
    with open(file_path, "r") as file:
        data = json.load(file)

        # Case 1: If it's a dictionary → convert to list
        if isinstance(data, dict):
            data = [data]

        # Case 2: If it's not a list (corrupt or weird)
        elif not isinstance(data, list):
            data = []

except (FileNotFoundError, json.JSONDecodeError):
    # Case 3: File is empty or doesn't exist
    data = []

# Now ALWAYS safe to append
data.append(weather_info)

with open(file_path, "w") as file:
    json.dump(data, file, indent=4, sort_keys=True)

for k, v in weather_info.items():
    print(f"{k}: {v}")

logger.info(f"City: {weather_data['name']}")
logger.info(f"Temperature: {weather_data['main']['temp']}°C")
logger.info(f"Humidity: {weather_data['main']['humidity']}%")
logger.info(f"Condition: {weather_data['weather'][0]['description'].title()}")
logger.info(f"Wind Speed: {weather_data['wind']['speed']} m/s")
