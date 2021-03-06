#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 09:39:49 2022

@author: dsmishler
"""

"""
Objectives:
    - Interactions between classes
    - Defensive programming
    - Write to a coup file
"""

"""
Instructions:
    - Copy this whole file into your own directory
    - Remove the instructor's name from the top and place your name
        - do the same with creation date
    - Follow the problem specifications that follow and make a python
      document that can run without any errors
    - For a hope score, push your homework to github by Sunday at 8:00 PM
        - If you submit after that, it's fine, but you get 0 marks if
          I grade and don't find your homework
"""


"""
Michael, Philip, and Thomas can skip problem 1 if they wish
"""
# Problem 1
# Write a function that takes a string as an argument
# Returns: the longest substring in that string after splitting the string
#          based on spaces.
# Example: my_func("hello world my name is Daniel")
#          returns: "Daniel"

# Problem 2
# In any way you see fit, find a way to *programmatically* determine whether
# the 8 files `game_*.coup` are valid games.
# You probably won't directly use this in your coup Game_Master,
# but you'll definitely implement a better game master with this knowledge.
# Recommendation: write some helper functions that are modular and easily
#                 usable in your coup.py file you'll make later on.

# Problem 3
# Build yourself a 'coup' directory and make a file called coup.py there.
# Build a player class in coup.py
    # Data
        # Coins
        # Cards
        # log ### Whenever the game writes to its game file, it also writes
              ### to each player's log
    # act()
        # If you have fewer than 7 coins, tax. Else, coup another player
        # You might have to parse the log to find another active player's name.
        # When I say "tax", I mean this method should return the string "tax"
        # or "coup markus"
        # don't forget that the first line of a log will be the list of
        # players playing the game!
    # receive()
        # arguments: a message
        # add that message to the log


# Problem 4
# Copy over your deck class from practice 2 to coup.py
# Add the draw() method, which returns the first (top) card in the deck
# and then removes that card from the deck

# Problem 5
# Build a class Game_Master in coup.py
    # Data:
        # players
        # log (just like the players)
        # deck
    # Methods:
        # game_init() (Note, this is *not* the __init__ function)
            # Arguments: the names of the players
            # Initializes the deck with 15 cards(they can all be dukes for now)
            # Give each player 2 cards and 2 coins
        # turn()
            # Determine the active player, and prompt them for an action
            # Process one action, such as "a tax" or "markus steal daniel"
            # Check to see whether that action was valid
            # Write that action to a gamefile and each player's log
            # If a player had to discard, also write that action to a gamefile
            # Update player cards and coins accordingly
        # game()
            # initialize a game and call turn() until the game is over
            # write the game log to a gamefile
                # by default, call it "coup_game_test.coup"
# Play a FFA game with 3 players and submit the file in your practice_3
# directory (since your Game_Master class lives in another directory)

"""
The following problem is for Michael, Thomas, and Philip
"""
# Problem 6
# Assume your player class only plays 1v1 coup.
# What is the optimal strategy for a no blocking, no challenging coup?
# Adjust your player class to adopt this strategy.
# To receive 4/4 on this assignment, I must *not* be able to design
# An agent to beat your player (no matter who goes first)