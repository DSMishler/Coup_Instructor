# -*- coding: utf-8 -*-
"""
Created on Thu May 26 14:49:42 2022

@author: Daniel Mishler
"""



# Problem 5
# Background: Random numbers are generated in the following way:
    # An initial global random number is chosen. That is called the 'seed'.
    # Then, a periodic function has that number switch to another number
    # in the range of [0, RAND_MAX]. Usually, RAND_MAX is 2**32-1. This means
    # that the number will switch to some number in the range [0,4294967295]
    # and that all 4294967296 numbers will be visited before the seed returns
    # to its initial value.
    # When you ask for a random number between, say, 1 and 2, Python will
    # sent the seed to its next value, then if the seed was odd, say,
    # Python will return you a 2. If it was even, say,
    # Python will return you a 1. You can think of this generation as
    # "coloring" the possible range that the seed might occupy.
    # This is a clever way to shrink the large range to give you seemingly
    # random numbers in a small range.
    # Try it for yourself! This code will generate the same random numbers
    # every time! On my machine, they are: `7, 10, 12`
import random
random.seed(66)
print(random.randint(6,16))
print(random.randint(6,16))
print(random.randint(6,16))

# Problem:
# Find a seed that gets the code over in generate_random.py
# to make a file that match thees following output:
"""
15
27
36
10
"""
# Hint: you may want to create a script that checks many seeds for you
# Note: do not change randfile.txt, but you can copy+paste the code over here
#       if you wish





# Problem 6
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


# Problem 7 (continuing problem 6)
# How many times should you expect the dog will want to play each day?
# How about going outside?
# How about eating?
# How about napping?
# Test over 100 days:
# How many hours long is the dog's day on average?