#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    # fileCreation: allows user to create a .cvs file with current beam data 
    #
    # Input:    beamLength: Length of beam [m] (scalar)
    #           loadPositions: Position of the load [m] (vector)
    #           loadForces: Force of the load [N] (vector)
    #           beamSupport: Support of beam (string), equal to both or cantilever.
    #           Prompt (file name)
    # Output:   File with current beam data as a table

import numpy as np
import pandas as pd

def fileCreation(beamLength, loadPositions, loadForces, beamSupport):
    
    # Input file name
    fileName=str(input("Please enter the file name (without extension): \n"))
    fileName=fileName+".csv"

    # Adds empty space in beamLength and beamSupport columns to fit table size
    if len(loadPositions) != 0:
        beamLength=np.append(beamLength, [None]*(len(loadPositions)-1))
        beamSupport=np.append(beamSupport, [None]*(len(loadPositions)-1))
        
    # If no load is present loadPositions and loadForces columns are set empty
    else:
        loadPositions=[None]
        loadForces=[None]

    # Create .csv file
    data = {'beamLength':beamLength, 'beamSupport':beamSupport, 'loadPositions':loadPositions, 'loadForces':loadForces}
    df = pd.DataFrame(data)
    df.to_csv(fileName)
    print("The file was created as",fileName)
    
    
