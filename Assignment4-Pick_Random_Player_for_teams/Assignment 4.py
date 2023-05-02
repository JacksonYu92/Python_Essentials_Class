"""
author: Qichun Yu
course: Python Essentials
description: Build a simple program to pick random players for two teams.
"""

from random import choice

# Variable to store a list of players, add players from players file
players = []
file = open('players.txt', 'r')
players = file.read().splitlines()
print('Players: ', players)

# Create variable to store a list of team names
teamNames = ['Alligators', 'Gorillas', 'Eagles', 'Pythons', 'Wasps', 'Panthers']
print('Team names: ', teamNames)

# New empty list to store players for each team
teamA = []    
teamB = []

# A loop to keep choosing players until no more players in the players list
while len(players) > 0:
    playerA = choice(players)     # Choose a random player
    teamA.append(playerA)         # Add player to team A
    players.remove(playerA)       # Remove player has been chosen

    if players == []:             # Tell program to stop when list empty
        break

    playerB = choice(players)     # Choose a random player
    teamB.append(playerB)         # Add player to team B
    players.remove(playerB)       # Remove player has been chosen 

# Choose a random name for each team
teamNameA = choice(teamNames)
teamNames.remove(teamNameA)
teamNameB = choice(teamNames)

# Print out players for each team
print()
print('Here are your teams: ')
print()
print(teamNameA, teamA)
print(teamNameB, teamB)
