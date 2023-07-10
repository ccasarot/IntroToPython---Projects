#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""


# MAIN 
#
# Interactive menu that allows user to use the code in all its functions
#    
# Input: Prompt, name of the file
#
# Output: Configured beam and loads and option to save them into a file
#         Generate plots from the input data
    

from beamPlot import beamPlot
from displayMenu import displayMenu
from fileCreation import fileCreation
from dataLoad import dataLoad
from configureLoad import configureLoad
import numpy as np


# Initializing variables
menuItems = (["Configure beam", "Configure loads", "Save beam and loads", "Load beam and loads", "Generate plot", "Quit"])
beamLength=10
beamSupport='Both'
loadPositions=np.array([])
loadForces=np.array([])

# Interactive menu starts
while True:
    choice = displayMenu(menuItems)
    
    #1. Configure beam
    if choice == 1:       
        while True:     
            try:
                beamLength = float(input("Please enter the beam length [m]: \n"))
                if (beamLength<0):
                    print("Beam length cannot be negative.")
                    beamLength=10
                    raise ValueError
                subMenuItems = (["Both","Cantilever"])
                print("Please enter the type of support:")
                beamSupport = displayMenu(subMenuItems)
                beamSupport=subMenuItems[int(beamSupport)-1]
                print("Beam length set to",beamLength,"[m] with support:",beamSupport)
            except ValueError:
                print("Non Valid input. Please try again.\n")
                continue
            break

    #2. Configure loads
    elif choice == 2:
        beamLength, beamSupport, loadPositions, loadForces = configureLoad(beamLength, beamSupport, loadPositions, loadForces) 
        
    #3. Save beam and loads  
    elif choice == 3:
        fileCreation(beamLength, loadPositions, loadForces, beamSupport)
            
    #4. Load beam and loads                    
    elif choice == 4: 
        while True:
            try:   
                beamLength, beamSupport, loadPositions, loadForces = dataLoad()  
                break
            except FileNotFoundError:
                print("No such file in the directory, please try again\n")
                continue
            
    #5. Generate plot    
    elif choice == 5: 
        beamPlot(beamLength, loadPositions, loadForces, beamSupport)

    #6. Quit
    elif choice == 6:
        print("Adios amigos")
        break 


