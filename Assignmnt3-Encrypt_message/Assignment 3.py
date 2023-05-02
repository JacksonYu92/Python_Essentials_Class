"""
author: Qichun Yu
course: Python Essentials
description: Build a simple program to encrypt message.
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'         # Create a variable to store a to z

message = input('Please enter a message: ')     # Ask user to enter a message
key = int(input('Enter a key (1-26): '))        # Allow user to enter a number between 1 - 26
newMessage = ''                                 # Variable to store the new encrypted message

# Use for loop to repeat for each character in the message
for character in message:
    if character in alphabet:
        position = alphabet.find(character)          
        newPosition = (position + key)%26       # Use % to go back to index 0 if over 26
        newCharacter = alphabet[newPosition]
        #print('The new character is: ', newCharacter)
        newMessage += newCharacter
    else:
        newMessage += character                 # Don't encrypt if not in the alphabet

print('Your new message is: ', newMessage)      # Print the encrypted message




  
