"""
author: Qichun Yu
course: Python Essentials
description: Build a program to fetch the last weather recording from a station.
"""
from requests import get          
import json                       
from pprint import pprint         

# url to access weather stations data to get latest weather measurements
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/1648902'

# Fetch the data and translate it into Python dictionaries
weather = get(url).json()['items']

# Use pprint module to make data easier to read
pprint(weather)
