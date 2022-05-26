# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:26:21 2022

@author: Daniel Mishler
"""

import random
# random is a library used for generation of random numbers
# such randomness functions are not in the default namespace of Python.
# Question: Why not import everything all tihe time?
# Answer: this modularization makes Python run faster. If Python
#         came with everything imported by default, it would run slower
#         because of the extra "bloat".

abab_file = open("abab.txt", 'w')

for i in range(500):
    # Generate a random number in [0,1,2]. If it happens to be 0
    # (in other words, 1/3 of the time)  :
    if(random.randint(0,2) == 0):
        abab_file.write("a")
    else:
        abab_file.write("b")


abab_file.close()