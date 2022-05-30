# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:32:49 2022

@author: Daniel Mishler
"""

"""
Objectives:
    - Understand what the terminal is and how to run a written python program
    - Understand basic usage of random numbers
    - Understand basic string parsing
    - Understand basic file input and out with open() and .close()
    - Understand how to build a class
    - Understand how to build and parse a text file
    - Programming philosophy: Understand defensive programming
"""

"""
Instructions:
    - Copy this whole file into your own directory
    - Remove the instructor's name from the top and place your name
        - do the same with creation date
    - Follow the problem specifications that follow and make a python
      document that can run without any errors
    - If you want some extra practice, proceed to the extra practice document
"""

# Problem 1
# Print a random whole number in the range of [1,10] (inclusive)

# Problem 2
# Print all of the perfect squares in the range of [1,10000]
# Note: you should use a loop (100 print statements will get you 0 points),
#       but you don't have to use 'for i in range(10000)' as your statement

# Problem 3
# Open the file `abab.txt` and print the total number of times the character
# 'b' appears in the file
# This shouldn't be hard-coded. You should be printing from a variable!
# Don't forget to close the file when you're done!
# Note: you're allowed to look at how the file was generated if you want


# Problem 4
# Open the file `abab.txt` and print the following:
    # the longest sequence of 'a's in the file
    # the longest sequence of 'b's in the file


# Problem 5
# Make a `dog` class that has the following data:
    # hunger (an integer that starts at 5)
    # manicness (an integer that starts at 3)
    # bathroom (an integer that starts at 2)
    # tiredness (and integer that starts at 0)
# And the following methods:
    # hour()    (simulating an hour passing for the dog)
        # the hour method should:
            # increase hunger randomly by [1,4]
                # If the dog's hunger goes to or above 10, the dog will eat
                    # Then the dog's hunger is set to 0
            # change the manicness randomly by [-2,+5]
                # Manicness cannot go below 0
                # If manicness goes to or above 10, the dog will play
                    # Then the dog's manicness is set to 3
                    # Then the dog's tiredness inceases by 2
                # If manicness goes to 0, the dog will take a nap
                    # Then the dog's manicness is set to 3
                    # Then the dog's tiredness decreases by 1
            # Change the bathroom randomly by [2,4]
                # If the dog's bathroom level goes to or above 10, the dog will
                # Go outside to releive itself
                    # Then the dog's bathroom level is set to 0
            # Change the tiredness randomly by [1,2]
                # If the tiredness goes to or above 26, the dog will go to bed
                    # Then reset hunger, manicness, bathroom, and tiredness
                    # to their default values
        # returns: you may have `hour()` return whatever you would like

# Now instantiate a `dog`, and do the following:
    # Open a text file called `dog_day.txt`
    # Write a line to the text file when any of the following happens
        # The dog wakes up
        # The dog goes out
        # The dog eats
        # The dog takes a nap
        # The dog plays
        # The dog goes to bed
    # Call the `hour` method until the dog goes to sleep
    # Have that file pushed to your repository so that I can see it as well,
    # *or* have the code which generates that file still here.
    # You may generate other files if you wish, but you must have at least
    # one `dog_day.txt`
# Recommendation: implement this as a `day` method.
# Recommendation: defensive programming
# Note: there are many ways to solve this question. You can add more to the
#       `dog` class, but you must have at least what was listed.