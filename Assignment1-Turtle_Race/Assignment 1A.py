# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 11:56:59 2022

@author: Qichun Yu
"""

from turtle import *
from random import randint

# make the turtle go faster
speed(0)
# move the turtle to the top left
penup()
goto(-140,140)

for step in range(15):
    write(step, align='center')
    right(90)
    for line in range(8):
        penup()
        forward(10)
        pendown()
        forward(10)
    penup()
    backward(160)
    left(90)
    forward(20)

ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160,100)
ada.pendown()

# do a twirl
for turn in range(10):
    ada.right(36)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160,70)
bob.pendown()

for turn in range(5):
    bob.left(72)

green = Turtle()
green.color('green')
green.shape('turtle')

green.penup()
green.goto(-160,40)
green.pendown()

for turn in range(20):
    green.right(18)

yale = Turtle()
yale.color('yellow')
yale.shape('turtle')

yale.penup()
yale.goto(-160,10)
yale.pendown()

for turn in range(3):
    yale.left(120)

for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    green.forward(randint(1,5))
    yale.forward(randint(1,5))






