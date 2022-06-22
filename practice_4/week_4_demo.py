# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 14:45:08 2022

@author: Daniel Mishler
"""

# Goals
    # Cover the coup infrastructure
        # Go over solution code
    # Cover how the coup infrastructure will change
        # Go over design decisions
    # Talk about plans for next week
    # Mutables
    # Demo: classes, self variables and self functions
    # dictionaries
    # splicing

# mutables
def change_it(a):
    if type(a) is int:
        a = 8
    if type(a) is list:
        a.append("another element")
    return

# mutables - like telling someone to remodel your house
# functions - like telling someone to bring something to you

# things that are mutables:
    # user-defined classes
    # lists


# Don't know what .copy() does?
# TL;DR - you probably don't need it, *but*
# active_players is a mutable, meaning that it's a special kind of
# variable that *does* remember what it was set to a while ago
# if a = b + c, then you change c, a will not change. But if the
# variable a was a mutable, then a *would* change. This .copy()
# makes active_players not behave like a mutable.

# Another way to make it immutable: mylist[:]



# classe and *self*

class Human:
    def __init__(self, given_name):
        self.name = given_name
    def change_name(self, changed_name):
        name = changed_name
        # variables which are defined in the scope of a function (in this case
        # it's a method in the Human class) don't live on past that function's
        # lifetime.
    def really_change_name(self, changed_name):
        self.name = changed_name
    def greet(self):
        print("Hello, my name is", self.name)


danny = Human("Danny")


# Dictionaries
# TL;DR; lists that are indexed by whatever you want
# []: list
# {}: dict

mydict = {}

mydict[1] = "data1"
mydict[6] = "data2"
mydict[1] = "data3" # overwrite key 1

# You can also index them with strings
mydict["goggins"] = "a man who works out and stays hard"

# remove something?
mydict.pop(1)

# just some food for thought

squares = {}
cubes = {}
for i in range(100):
    squares[i] = i*i
    cubes[i] = i*i*i

math = {}
math["squares"] = squares
math["cubes"] = cubes


# splicing
print("hello"[:4]) # long dictionaries lead you here

# splicing takes a string or list and gives you element a up to but
# not including element b
a = 0
b = 7
print("hello world"[a:b])

# if a is missing, it's assumed 0
# if b is missing, it's assumed the whole array

# Pieces of caution when editing your coup file:
    # 1: error check action legality
    # 2: error check forcing a player to discard
    # 3: defensive programming, test often
    # 4: make it fun to use