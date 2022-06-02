# -*- coding: utf-8 -*-
"""
Created on Mon May 30 10:18:14 2022

@author: Daniel Mishler
"""

# Outline:
# Teaching philosophy
    # Be interactive
    # Why am I doing this?
    # Grading
    # Availability
    # How do you know you're learning?
# Github
    # Why github?
    # How to use?
        # commit, push
        # github desktop makes it easy
# The terminal:
    # 'print'
    # variables (if I type anything that's not reserved, it's a variable)
        # int
        # bool
        # str
        # float (we won't use these much)
        # list
    # assignment (=) (think of it more like a left arrow <-)
    # Golden Rule #1:
"""
        only that which you specifically changed shall change
"""
    # types with 'type'
    # assumed print in terminal
# The file
    # Running the file
    # Golden Rule #2
"""
        defensive programming is key to a good understanding of fundamentals
"""
    # Unless you're dead sure the code you've written is correct, it's always
    # a good idea to double check stuff.
    # Change, Predict, Check
# Conditionals
    # if
    # else
    # elif
    # `True` and `False`
# Loops
    # while
    # for
# File I/O
    # open
        # writing
            # over-writing
        # reading
        # appending
    # close
        # note: always close (it's good practice)
# Classes
    # data
    # methods
    # example: cat
        # restlessness
        # hunger
        # go_away()
        # feed()
        # play()
# importing stuff
    # random
    # There are other ways
        # from `a` import `b`
        # from `a` import *
        # import `a` as `c`
    # How are random numbers generated?

# Practice announced
# How do you know you're doing well?



a = 1
b = 2
c = a + b
print(c)
a = 6
print(c)
print(a)


# < is not the only thing
# We've got...
# <=
# >=
# != (not equal to)
# == (equal to)
if(a < c):
    print("True")
else:
    print("You got caught lackin'")



'''
while(1 == 1):
    print("hello world")
    # maybe there's many lines...
    # click terminal and Ctrl+C to stop a program
'''


a = 0
while(a < 10):
    print("hello world")
    a = a + 1
    # think of = as a <-


myList = ["apples", "oranges"]

for item in myList:
    print(item)



for i in range(10):
    print(i, "sqaured is", i*i)


# open: takes file name and one more letter:
    # w: write (over-write)
    # r: read
    # a: append


myFile = open("newfile.txt", "a")
myFile.write(" this is appended text!")
myFile.close()


readFile = open("newfile.txt", "r")
print(readFile.read())
readFile.close()



import random

print(random.randint(0,10))



# Tips for homework 1
for character in "hello":
    print(character)
    if(character == "l"):
        print("character was an l")