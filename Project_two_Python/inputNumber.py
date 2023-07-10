#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    # inputNumber prompts the user to imput a number
    #
    # usage: num=imputnumber(prompt) Displays prompts and asks user to choose a number.
    # repeats until the user inputs a valid number
    #
    # author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    
def inputNumber(prompt):
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num