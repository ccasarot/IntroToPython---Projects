#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    #beamSuperposition similar as beamDeflection, but it creates a superposıtıon of 
    #                  deflections for several loads in different positions at a time.
    #
    #Input: positions:(type: array of floats) All the different points along the beam where deflection
    #                     is being calculated for every elements of it.
    #       beamlength:(type: float)Length of the beam.(m)
    #       loadPositions:(type: array of floats) The position of the loads from the very left point.(m)
    #       loadForces:(type: array of float) The magnitude of the loads.(kN)
    #       beamSupport:(type: integer)Numbers correlating to beam types.(1 for both end type,2 for 
    #                       cantilever)
    #Output: deflection:(type: array of floats) Deflections correlating to every points of the 
    #                       positions vector.

import numpy as np
from beamDeflection import beamDeflection

def beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport):
    
    deflections = np.zeros(len(positions))
    i = 0
    for element in loadPositions:
        deflections = deflections + beamDeflection(positions, beamLength, element, loadForces[i], beamSupport)
        i = i + 1
        
    return deflections

