"""

# The script supports a " --help" option which outputs the following text:

Fetch weather information

Usage: 
      weather (-h | help)
      weather [--country=COUNTRY] <city>
      
Options:
      --h, --help               Show a brief usage summary
      --country=COUNTRY         Restrict cities to an ISO 3166 country code
      
"""    

import requests
import docopt
import os
from datetime import datetime
from decimal import *

# Convert temperature from Kelvin to Degrees Celsius - [°C] = [K] − 273.15
def temp_kelvin_to_celsius(temp_in_kelvin):
    return decimal(temp_in_kelvin) - decimal(273.15)

# API Call & Parameters requested from the API response
def fetch_weather(city_name, country_code, api_key):

# Build URL query depending on if there is a country or not - It restricts cities to an ISO 3166 country code
    if country_code:
        query = {"q":city_name + "," + country_code, "app_id":api_key}
    else:
        query = {"q":city_name, "app_id":api_key}

# Get data from openweathermap.org & passing parameter in URL
request = requests.get('https://api.openweathermap.org/data/2.5/weather', params=query)

# Check that the URL has been correctly encoded by printing the URL
print(r.url)

# Check the HTTP response status code - If there is a staus_code = 200 - then we have a valid response
status = r.status_code

# If HTTP status code is = 200 (Valid response)
if r.status_code == 200:
response = r.json()
# Print (response)
# Print (response)["main"]["temperature"]
      temperature = temp_kelvin_to_celsius(response["main"]["temp"])
      max_temperature = temp_kelvin_to_celsius(response["main"]["temp_max"])
      min_temperature = temp_kelvin_to_celsius(response["main"]["temp_min"])
      humidity = response["main"]["humidity"]
      clouds = response["all"]["clouds"]
      rain = response["h1"]["rain"]
      sunrise = response["sys"]["sunrise"]
      sunset = response["sys"]["sunset"]
      country = response["sys"]["country"]
      json = response
# Otherwise if there is an error in the status code then return status code and blank temperature
else:
      status = r.status_code
      temperature = ""
      max_temperature = "" 
      min_temperature = ""
      humidity = ""
      clouds = ""
      rain = ""
      sunrise = "" 
      sunset = ""
      country = ""
      json = ""
      
# Return a dictionary
currentweather = {}
currentweather = "temperature"
currentweather = "max_temperature"
currentweather = "min_temperature"
currentweather = "humidity"
currentweather = "clouds"
currentweather = "rain"
currentweather = "sunrise"
currentweather = "sunset"
currentweather = "country"
currentweather = "json"
      
# The option parser is generated based on the docstring above that is passed to docopt function
if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
