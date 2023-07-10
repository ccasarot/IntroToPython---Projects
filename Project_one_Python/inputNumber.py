#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
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