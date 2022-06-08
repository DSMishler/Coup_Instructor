# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:03:26 2022

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


# List

myList = [1,2,3]

myList.append(4)

for character in "hello":
    myList.append(character)
    
# Index list elements by their number, *starting with 0*
# negative numbers: from the end

myList.append([1,2])

def is_perfect_square(x):
    for i in range(x):
        if(x == i*i):
            return True
    return False

 # Fun challenge: why did I skip the number 1?
for i in range(101):
    if is_perfect_square(i):
        print(i)


# Functions can be passed *anything* and they can return *anything*
def lots_of_arguments(a, b, c, d, e, f, g):
    # Can I check variables are of a certain type?
    if(type(c) is not str): # warning condition
        print("warning, I expected variable c to be string")
    
    if(type(d) is not str): # error condition
        print("error: expected d to be string, but d is not string")
        return "Error"
    
    print(a,b,c,d,e,f,g)
    print(g)
    newVariable = c + d
    print(newVariable)
    
    # as an aside: all function that don't say `return` at the end
    # python assumes that you meant this:
    return None


# argument defaults
# if nothing was passed to the function, don't throw an error, instead
# just run the function with those parameters
# You won't need to know default arguments to pass the class
# You can write a perfectly good coup agent with it
def default_args(a = 1, b = 5):
    print(a, b)
    return (a+b)


# scope
my_var = 0
def change_function(a):
    print(a)
    a= 10
    print(a)

def return_sum(a,b):
    return a+b

def confusing_combine(a,b):
    answer = a + b
    a = 10
    b = 11
    return answer

programs_a = 4
programs_b = 5
programs_ans = 0

programs_ans = confusing_combine(programs_a,programs_b)

# '\n': newline
print("a:", programs_a, end = "   ")
print("b:", programs_b, end = "   ")
print("ans:", programs_ans, end="\n")

# passing functions
def call_twice(func_to_call):
    func_to_call()
    func_to_call()

class Cat:
    # init is a special function which is always called when the class is
    # initialized
    def __init__(self, cat_name):
        self.hunger = 0
        self.size = 5 # pounds
        self.name = cat_name
    def meow(self):
        print("meow")
    def nametag(self):
        print("the cat's name tag says '" + self.name + "'")
    def bulk(self):
        print("MEOW")
        self.size = self.size + 1
        self.hunger = 0
    def fight(self, othercat):
        print(self.name, "vs", othercat.name)
        print("FIGHT")
        if(self.size > othercat.size):
            print(self.name, "is victorious!")
        elif(self.size < othercat.size):
            print(othercat.name, "is victorious!")
        else:
            print("it's a stalemate!")



# You can have multiple instances of a class, which are individually
# initialized like so
mycat_1 = Cat("trey")
mycat_2 = Cat("boo")


def catfight(cat_a, cat_b):
    print(cat_a.name, "vs", cat_b.name)
    print("FIGHT")
    if(cat_a.size > cat_b.size):
        print(cat_a.name, "is victorious!")
        return cat_a
    elif(cat_a.size < cat_b.size):
        print(cat_b.name, "is victorious!")
        return cat_b
    else:
        print("it's a stalemate!")
        return None


# (terminal tip: use up arrows to repeat things in terminal)