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

def is_perfect_square(x):
    for i in range(x):
        if(x == i*i):
            return True
    return False

for i in range(1000):
    if is_perfect_square(i):
        print(i)