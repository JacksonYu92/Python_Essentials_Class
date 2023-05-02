#!/bin/python3
import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?.:;[]{}()_*&^%$#@!~+-*/'

print("Password Generator")
print("==================\n")

numberOfPasswords = int(input('number of passwords? '))
length = input('password length? ')
length = int(length)

print()
print('here are your passwords: ')
for p in range(numberOfPasswords):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
