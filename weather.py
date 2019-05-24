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
def temperature_kelvin_to_celsius(temp_in_kelvin):
    return decimal(temp_in_kelvin) - decimal(273.15)

# API Call & parameters
def fetch_weather_(city_name, country_code, APPID)

# Build URL query depending on if there is a country or not
    if country_code:
        query = {"q":city_name + "," + country_code, "APPID":API_key}
    else:
        query = {"q":city_name, "APPID":API_key}

# Get data from openweathermap.org & passing parameter in URL
r = requests.get(‘api.openweathermap.org/data/2.5/weather’, params=query)

# The option parser is generated based on the docstring above that is passed to docopt function
if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
