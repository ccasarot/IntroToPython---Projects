#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    # dataLoad: allows user to load a .cvs file and configure a beam with its content
    #
    # Input:    Prompt (file name)
    #
    # Output:   Beam data loaded from file 

import numpy as np
import pandas as pd

def dataLoad():
    
    # Prompts user for file name
    loadFile=str(input("Please enter the .csv file name (without extension): \n"))
    loadFile=loadFile+".csv"
    file = pd.read_csv(loadFile)
    
    # Imports file data into beam
    try:
        beamLength=file["beamLength"]
        beamSupport=file["beamSupport"]
        loadPositions=file["loadPositions"]
        loadForces=file["loadForces"]
        beamLength=int(beamLength[0])
        beamSupport=str(beamSupport[0])
        loadPositions=np.array(loadPositions)
        loadForces=np.array(loadForces)
        # Sets as empty void cells
        if (np.any(np.isnan(loadPositions)==True)) or (np.any(np.isnan(loadForces)==True)):
            loadPositions=np.array([])
            loadForces=loadPositions
    
    # Error handling 
        if (beamLength<0):
            print("beamLength cannot be negative")
            raise ValueError
        if (beamSupport!="Both") & (beamSupport!="Cantilever"):
            print("Check spelling of beamSupport")
            raise ValueError
        if np.any(loadPositions<0) or np.any(loadPositions>beamLength):
            print("Loads cannot be outside the beam")
            raise ValueError
        if np.any(loadForces<0):
            print("Loads cannot be negative")
            raise ValueError
        print(loadFile,"loaded correctly")
    # Groups any invalid data input
    except BaseException:
        print("Load file failed: input file is compromised")
    
    return beamLength, beamSupport, loadPositions, loadForces



