"""
author: Qichun Yu
course: Python Essentials
description: Build a program to find the distance between two points on the Earth.
"""
from math import radians, cos, sin, asin, sqrt

# A function to find the distance between two points on the earth.
def haversine(lon1, lat1, lon2, lat2):
    #convert degrees to radians
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lon2 = radians(lon2)
    lat2 = radians(lat2)

    #difference between the two longitudes and latitudes
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    #haversine formula
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    distance = 2 * asin(sqrt(a)) * 6371      #6371 is the radius of the Earth
    return distance
