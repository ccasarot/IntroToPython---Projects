#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    # configureLoad: allows user to configure loads on beam 
    #                  through an interactive menu
    #
    # Input:    beamLength: Length of beam [m] (scalar)
    #           loadPositions: Position of the load [m] (vector)
    #           loadForces: Force of the load [N] (vector)
    #           beamSupport: Support of beam (string), equal to both or cantilever.
    # Output:   Beam with configured loads

import numpy as np
from displayMenu import displayMenu

def configureLoad(beamLength,beamSupport,loadPositions,loadForces):
    while True:
            subMenuItems = (["See the current loads", "Add a load", "Remove a load", "Return to main menu"])
            subChoice = displayMenu(subMenuItems)
            
            # See current loads
            if subChoice==1:
                if len(loadPositions)==0:
                    print("No load currently present. Please add a load")
                    continue
                print("Beam length =", beamLength,"meters, current loads:")
                for i in range(len(loadPositions)):
                    print("Load number",i, "position",loadPositions[i], "[m] and force",loadForces[i],"N")
                    continue
                
            # Add a load     
            if subChoice==2:
                while True:
                    try:
                        inputLoadPosition = float(input("Please enter the load position: \n"))
                        if (inputLoadPosition<0) or (inputLoadPosition>beamLength):
                            print("Loads cannot be outside the beam.\n")
                            continue
                        loadPositions = np.append(loadPositions,inputLoadPosition)
                        break
                    except ValueError:
                        print("Invalid input. Please try again\n")
                        continue
                while True:
                    try:
                        inputloadForce = float(input("Please enter the load force: \n"))
                        if inputloadForce<0:
                            print("Forces cannot be negative.\n")
                            continue
                        loadForces = np.append(loadForces,inputloadForce)
                        break
                    except ValueError:
                        print("Invalid input. Please try again\n")
                        continue
                    
            # Remove a load        
            if subChoice==3:
                while True:
                    try:
                        if len(loadPositions)==0:
                            print("No load currently present. Please add a load")
                            break
                        removedLoad=int(input("\nPlease indicate the load to be deleted (load index start from 0): \n"))
                        if removedLoad<0:
                            raise IndexError
                        loadPositions=np.delete(loadPositions,removedLoad)
                        loadForces=np.delete(loadForces,removedLoad)
                        print("load",removedLoad,"successfully removed")
                        break
                    except (IndexError, ValueError):
                        print("Invalid input. Please try again")
                        continue  
                    
            #Back to main menu        
            if subChoice==4:
                break

    return beamLength, beamSupport, loadPositions, loadForces












