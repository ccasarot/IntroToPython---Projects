#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

# beamDeflection: calculates deflection of beam at given position 
#
# Input:    positions: Positions [m] to compute the beam deflection (vector)
#           beamLength: Length of beam [m] (scalar), below denoted l.
#           loadPosition: Position of the load [m] (scalar), below denoted a.
#           loadForce: Force of the load [N] (scalar), below denoted W.
#           beamSupport: Support of beam (string), equal to both or cantilever.
# Output:   deflection as a vector 

import numpy as np

def beamDeflection(positions, beamLength, loadPosition, loadForce, beamSupport):
    
    # Initializing variables
    x=positions 
    l=beamLength
    a=loadPosition
    W=loadForce
    E=200e9
    I=0.001
    deflection=np.zeros(len(x))
    
    # Calculate deflection depending on support type
    for i in range(len(x)):
        if beamSupport=='Both':
            if x[i]<a:
                deflection[i]=((W*(l-a)*x[i])/(6*E*I*l))*(l**2-x[i]**2-(l-a)**2)
            elif x[i]>=a:
                deflection[i]=((W*a*(l-x[i]))/(6*E*I*l))*(l**2-(l-x[i])**2-a**2)
        elif beamSupport=='Cantilever':
            if x[i]<a:
                deflection[i]=((W*x[i]**2)/(6*E*I))*(3*a-x[i])
            elif x[i]>=a:
                deflection[i]=((W*a**2)/(6*E*I))*(3*x[i]-a)
    return deflection
