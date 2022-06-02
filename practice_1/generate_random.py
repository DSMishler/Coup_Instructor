# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 12:08:49 2022

@author: Daniel Mishler
"""

import random
random.seed(0) # zero was not the seed used to generate the desired output.
randfile = open("randfile.txt", "w")
randfile.write(str(random.randint(0,99)))
randfile.write("\n")
randfile.write(str(random.randint(0,99)))
randfile.write("\n")
randfile.write(str(random.randint(0,99)))
randfile.write("\n")
randfile.write(str(random.randint(0,99)))
randfile.close()