"""
author: Qichun Yu
course: Python Essentials
description: Create a Deck class to display a deck of cards.
"""
from card import Card

class Deck:

    def __init__(self):
        self._cards = []         # Create an empty list to store a list of cards
        self.populate()          # Call the populate() method and print out the list
        print(self._cards)

    def __repr__(self):          # Use representation method to return a text of an object
        return str(self._cards)  # Turn it to string to aviod typeError

    def populate(self):
        suits = ["hearts", "clubs", "diamonds", "spades"]    # Create a list for possible card suits
        # Create a list for possible card numbers as strings
        numbers = [str(n) for n in range(2,11)] +["J", "Q", "K", "A"]
        cards = []                              # Create an empty list of cards
        for suit in suits:                      # Loop over each suit
            for number in numbers:              # Loop over each possible card number
                cards.append(Card(suit,number)) # create a new card object and add it to the list
        self._cards = cards                     # Then point self._cards at this list

        # Use list comprehension
        #self._cards = [ Card(s, n) for s in suits for n in numbers ]


# Create an instance of the Deck class to display the list 
my_deck = Deck() 
#print(my_deck)
