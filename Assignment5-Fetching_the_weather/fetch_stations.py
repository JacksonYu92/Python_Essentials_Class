"""
author: Qichun Yu
course: Python Essentials
description: Build a program to find a weather station.
"""
from requests import get          
import json                       
from pprint import pprint         

# url to access weather stations data to get all stations
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'

# Fetch the data and translate it into Python dictionaries
stations = get(url).json()['items']

# Use pprint module to make data easier to read
pprint(stations)
