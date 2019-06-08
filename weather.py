"""

# The script supports a " --help" option which outputs the following text:

Fetch weather information

Usage: 
      weather (-h | help)
      weather [--country=COUNTRY] <city>
      
Options:
      --h, --help               Show a brief usage summary
      --country=COUNTRY         Restrict cities to an ISO 3166 country code

An OpenWeatherMap API key MUST be provided in via the OPENWEATHERMAP_KEY environment variable.     

"""    

import requests
import os
from docopt import docopt
from datetime import datetime
from decimal import *

# Convert temperature from Kelvin to Degrees Celsius - [°C] = [K] − 273.15
def temp_kelvin_to_celsius(temp_in_kelvin):
    return decimal(temp_in_kelvin) - decimal(273.15)

# API Call & Parameters requested from the API response
def fetch_weather(city_name, country_code, api_key):

      # Build URL query depending on if there is a country or not - It restricts cities to an ISO 3166 country code
    if country_code:
        query = {'q': city_name + ',' + country_code, 'app_id': api_key}
    else:
        query = {'q': city_name, 'app_id': api_key}
# Get data from openweathermap.org & passing parameter in URL
r = requests.get('https://api.openweathermap.org/data/2.5/weather', params=query)

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
    # print(arguments)
    country = arguments["--country"]


# Get weather's information if OpenWeatherMap API key is obtained
try:
    apikey = os.environ['OPENWEATHERMAP_KEY']
except:
    print ("OPENWEATHERMAP_KEY API error")
    apikey = ""
    exit(1)

# Store the value of "city" key in variable: city   
city = argument["<city>"]

# Store the values of "city_name", "country_code" and "api_key" in variable: weather
weather = fetch_weather(city_name, country_code, api_key)
      
# Return weather information
if weather["status"] == 200:
    temp_in_celsius = weather["temp"]
    return_country = weather["country"]
    # Print the default output for city + country + temperature in celsius
    print("Temperature for " + city.title() + ", " + return_country.title() + ": " + str(temp_in_celsius) + u"\u2103")      
# Otherwise status code is = 401 (Unauthorised) or 404 (Not Found)
elif r.status_code == 401:
      print ("Error 401 - Not authorised")   
else:
      print ("Error 404 - Not found")
