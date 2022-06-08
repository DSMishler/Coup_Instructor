# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 15:05:32 2022

@author: Daniel Mishler
"""

"""
Objectives:
    - Lists
        - append
    - Understand functions
        - arguments
        - return value
        - scope
    - Understand classes
        - data
        - methods
        - make a sufficient example
"""

"""
Instructions:
    - Copy this whole file into your own directory
    - Remove the instructor's name from the top and place your name
        - do the same with creation date
    - Follow the problem specifications that follow and make a python
      document that can run without any errors
    - If you want some extra practice, proceed to the extra practice document
    - For a hope score, push your homework to github by Sunday at 8:00 PM
        - If you submit after that, it's fine, but you get 0 marks if
          I grade and don't find your homework
"""
import random

# problem 1
# write a function that takes two integers as an argument
# and returns their product. Call it whetever you would like


# problem 2
# fix up the below function to pass the tester
# hint: % is the remainder function.
    # 10 / 6 would be 1 and 4/6, so 
    # 10 % 6 would be 4
# Note: I intentionally left names to be a little confusing and left out
#       some comments. You should be able to figure it out nonetheless.

def mystery_function(a):
    return None

def problem_2_tester():
    for i in range(20):
        newarg = random.randint(1,1000)
        if(newarg % 2 == 1):
            newarg += 1 # `newarg += 1` is the  same as `newarg = newarg + 1`
        if(mystery_function(newarg) == True):
            # do nothing
            pass
        else:
            print("your function failed on iteration %d!" % i)
            print("argument:", newarg, "\nexpected value:", True)
            return

    for i in range(20):        
        newarg = random.randint(1,1000)
        if(newarg % 2 == 0):
            newarg += 1
        if(mystery_function(newarg) == False):
            # do nothing
            pass
        else:
            print("your function failed on iteration %d!" % i+20)
            print("argument:", newarg, "\nexpected value:", False)
            return
    
    
    print("your function passed!")
    return

# now call the function
problem_2_tester()


# Problem 3
# write a function called "tester_function"
    # arguments: `test_function`
    # returns:
        # `True` if `test_function` was one of the `correct_function`s
        # `False` if `test_function` was one of the `incorrect_function`s


def correct_function_1():
    return random.randint(1,4) * 8

def correct_function_2():
    return random.randint(7,1000) * 88

def correct_function_3():
    return random.randint(2,50) * 32

def incorrect_function_1():
    return random.randint(7,10) * 4 + 1

def incorrect_function_2():
    return random.randint(1,7) * 5

def incorrect_function_3():
    return random.randint(18,88) * 18 + 3








# Problem 4
# write a class called `Deck`
# with data
    # `cards` : initialized to an empty list
# and methods
    # `add`
        # arguments: a string
        # adds the string as a card to the `cards` list
            # remember: <list>.append(<b>) adds <b> to <list>
    # `show`
        # prints the deck
    # `shuffle`
        # shuffles the deck
        # hint: use your trusty internet capabilities to find out what
        #       `random.shuffle()` does


# Note: you *will* use this deck for Coup later on



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
# Note: if you have questions about what should happen first in an hour,
#       check things *in the order that I specified them*
# Note: there are many ways to solve this question. You can add more to the
#       `dog` class, but you must have at least what was listed.




"""
Problem 6 is optional
"""
# Problem 6 (continuing problem 5)
# How many times should you expect the dog will want to play each day?
# How about going outside?
# How about eating?
# How about napping?
# Test over 100 days:
# How many hours long is the dog's day on average?