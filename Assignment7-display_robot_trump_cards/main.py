"""
author: Qichun Yu
course: Python Essentials
description: Create a program to display robot trump cards by reading data from a file.
"""
from random import choice
from turtle import *

# Setup the screen and turtle
screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()

robots = {}  # Create a robots dictionary

file = open('cards.txt', 'r')  # Read data from cards.txt file

# Split the file into a list of lines, then loop over those lines
for line in file.read().splitlines():
    # Break down data for each individual robot and store into variables
    name, battery , intelligence, usefulness, speed, color, image = line.split(', ')
    # Use robot's name as a key to a dictionary
    robots[name] = [battery, intelligence, usefulness, speed, color, image]
    screen.register_shape(image)   # To register the image

file.close()

print("Robots:  rainbow, space, bird, jet, twoheads, dog, round, brains, tv, hair, shades, yellow (or random)")

# Use while loop to allow user to view different robots
while True:

    robot = input('Choose a robot: ')  # Ask user to entry the robot that they would like to see
    
    if robot == "random":              # Allow user to see a random robot
        robot = choice(list(robots.keys()))   # Randomly pick a key from the robots dictionary
        print(robot)

    # If robot exist in the dictionary then display its data, otherwise display an error
    if robot in robots:
        stats = robots[robot]          # Store the list of stats for the robot
        style = ('Arial', 14, 'bold')  # A variable to store font styles
        clear()                        # Clear screen before displaying another robot
        pencolor(stats[4])             # Display robot's data in different color
        
        goto(0,100)                    # Position and stamp the image
        shape(stats[5])
        setheading(90)
        stamp()
        setheading(-90)                
        forward(80)
        
        setheading(-90)                # Move the turtle so stats are not display on top of each other
        write('Name: ' + robot, font=style, align='center')            # Show robot's name
        forward(25)
        write('Battery: ' + stats[0], font=style, align='center')      # Show robot's battery data
        forward(25)
        write('Intelligence: ' + stats[1], font=style, align='center') # Show robot's intelligence data 
        forward(25) 
        write('Usefulness: ' + stats[2], font=style, align='center')   # Show robot's usefulness data
        forward(25)
        write('Speed: ' + stats[3], font=style, align='center')        # Show robot's speed data
    else:
        print('Robot doesn\'t exist!')
