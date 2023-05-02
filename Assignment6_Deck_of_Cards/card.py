"""
author: Qichun Yu
course: Python Essentials
description: Create a Card class that will act as a template for creating playing objects.
"""

class Card:
    
    def __init__(self, suit, number):
        self._suit = suit    #underscore indicate should not change this attribute directly
        self._number = number

    # Use representation method to return a text of an object
    def __repr__(self):     
        return self._number + " of " + self._suit

    # Creating a getter for suit, self._suit will be stored in my_card object
    @property
    def suit(self):
        return self._suit
    
    # Creating a setter for suit, now user able to set the suit attribute
    @suit.setter
    def suit(self, suit):
        # Check if the suit is a valid card suit
        if suit in ["hearts", "clubs", "diamonds", "spades"]:
            self._suit = suit
        else:
            print("That's not a suit!")

    # Creating a getter for number
    @property
    def number(self):
        return self._number

    # Creating a setter for number
    @number.setter
    def number(self, number):
        # Check if the number is a valid card number
        if number in ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]:
            self._number = number
        else:
            print("That's not a valid number!")

"""       
# Print out for testing   
my_card = Card("hearts" , "6")
print("My card:" , my_card)

my_card.suit = "diamonds"
print("The suit of my card is", my_card.suit)
print("My card:" , my_card)

my_card.suit = "dinosaurs"
print("My card:" , my_card)

my_card.number = "8"
print("The number of my card is", my_card.number)
print("My card:" , my_card)

my_card.number = "23"
print("My card:" , my_card)
"""
