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
# dog