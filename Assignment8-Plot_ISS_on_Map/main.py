"""
author: Qichun Yu
course: Python Essentials
description: Create a program to find out the current location of the International
Space Station(ISS) and plot its location on a map.
"""
import json
import turtle
import urllib.request
import time

# Use a web service to loop up the number of people in space and print it
url = 'http://api.open-notify.org/astros.json' # URL that has astronauts' data
response = urllib.request.urlopen(url)         # Call the web service
result = json.loads(response.read())           # Load JSON into Python data structure
print('People in Space: ', result['number'])

people =result['people']

# Print out a line for each astronaut
for p in people:
    print(p['name'],'in',p['craft'])

# Use web service to show the current location of ISS
url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

#Create variables to store the latitude and longitude, and print them
location = result['iss_position']
lat = float(location['latitude'])      # Turn string to float
lon = float(location['longitude'])
print('Latitude: ', lat)
print('Longitude: ', lon)

# Using Python Turtle graphics to plot the ISS on a map
screen = turtle.Screen()
screen.setup(720, 360)         # Set the screen size to match the size of the image
screen.setworldcoordinates(-180, -90, 180, 90)  # Set screen to match the coordinates that is using
screen.bgpic('map.gif')        # Load a world map as the background image

# Use iss image to represent the ISS, load it into turtle
screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

# ISS image go to the current location of ISS on a world map
iss.penup()
iss.goto(lon,lat)

# Space Center, Houston
lat = 29.5502
lon = -95.097

# Use turtle to plot a yellow dot on the map for Houston's location
location = turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

# Use web service to find out when the ISS will next be over the Houston
url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)    # Turn float to string and pass as input to the URL
response = urllib.request.urlopen(url)
result = json.loads(response.read())

over = result['response'][1]['risetime']   # A variable to store pass-over time as a Unix time stamp
#print(over)

style = ('Arial', 6, 'bold')
location.write(time.ctime(over), font=style)   # Use time.ctime() function to convert the time stamp

# Winnipeg's coordinates
lat = 49.8951
lon = -97.138

# Use turtle to plot a red dot on the map for Winnipeg
location.penup()
location.color('red')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

# Use web service to find out when the ISS will next be over the Winnipeg
url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# Convert time to a readable form and print it onto the map
over = result['response'][1]['risetime']
location.write(time.ctime(over), font=style)
