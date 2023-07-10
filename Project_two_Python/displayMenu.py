#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    # displayMenu displays a menu of options, ask the user to choose an item
    # and return the number of the menu item chosen
    #
    # Input: options, menu options (cell, array of strings)
    #
    # Output: choice (chosen option, float)

import numpy as np
from inputNumber import inputNumber

def displayMenu(options):
    print('')
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    choice = inputNumber("Please choose a menu item: \n ") 
    
    # condition if the input is wrong
    while not(np.any(choice == np.arange(len(options))+1)):
        choice = inputNumber("Invalid input. Please try again: \n ")
    return choice
