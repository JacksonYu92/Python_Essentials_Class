"""
author: Qichun Yu
course: Python Essentials
description: Build a program to fetch the last weather recording from a station that is the closest to Winnipeg.
"""
from requests import get
import json
from pprint import pprint
from haversine import haversine

# URLs to get the Weather Stations and the latest weather
stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

# Winnipeg's longitude and latitude
my_lat = 49.90
my_lon = -97.14

# Fetch the data and translate it into Python dictionaries
all_stations = get(stations).json()['items']

# A function to find the closest station
def find_closest():
    # Longest possible distance between two points on Earth is 20036km
    smallest = 20036   
    
    # Iterate through all the stations
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        # Use haversine function to find the distance
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        # Find the smallest distance one and save that station's ID
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station

# Create a variable to save the closest weather station ID
closest_stn = find_closest()

# Convert station ID to a string and concatenate with weather URL 
weather = weather + str(closest_stn)

# Fetch the weather data and translate it into Python dictionaries
my_weather = get(weather).json()['items']

# Use pprint module to make data easier to read
pprint(my_weather)
