#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  26 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""
    # Generates plot of the deflection-position graph
    #
    #Input:      beamlength:(type: float)Length of the beam.(meter)
    #           loadPositions:(type: array of floats) The position of the loads from the very left point.
    #                       (meter)
    #           loadForces:(type: array of float) The magnitude of the loads.(kN)
    #           beamSupport:(type: integer)Numbers correlating to beam types.(1 for both end type,2 for 
    #                       cantilever)
    #
    #Output:    Plots the deflection-position graph

import numpy as np
import matplotlib.pyplot as plt
from beamSuperposition import beamSuperposition

def beamPlot(beamLength, loadPositions, loadForces, beamSupport):
    
    # Creating variables for the plot of the beam
    x = np.arange(0., beamLength + beamLength/100, beamLength/100)
    y = beamSuperposition(x, beamLength, loadPositions, loadForces, beamSupport)
    
    # Creating variables for the plot of load points
    if loadForces.any():
        y2 = beamSuperposition(loadPositions, beamLength, loadPositions, loadForces, beamSupport)
    
    # Setting up the plot area
    fig = plt.figure()
    fig.set_figheight(10)
    fig.set_figwidth(10)
    
    # Plotting the beam 
    plt.plot(x, y, 'r-') 
    
    # Plotting positions of loads
    if loadForces.any():    
        plt.plot(loadPositions, y2, 'b*')
        
    # Measuring deflection downwards 
    plt.gca().invert_yaxis() 
    
    # Setting up title, labels, grid  and ticks 
    plt.title("Beam deflection\nBeam type: {:s}".format(beamSupport))
    plt.xlabel("Beam Length (m)")
    plt.ylabel("Deflection (m)")
    plt.xlim([0, 1.05*beamLength])
    plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.tight_layout()
    plt.grid(color='grey', linestyle='--', linewidth=0.5) 
    plt.axhline(y=np.max(y),linewidth=1, color='g')    
    
    # Sorting data for the legend
    if loadForces.any():
        force = np.array([(loadPositions[idx], loadForces[idx]) for idx in range(len(loadPositions))], dtype=[('pos',int),('force',int)])
        force.sort(axis=0, order=['pos'])
        force = np.array([np.array([i[0], i[1]]) for i in force])
        force = force[:,1] 
        
        #Making the string containing magnitudes 
        f_format = np.array([])
        for i in range(np.size(y2)):
            x = 'F{:d} = {:.2E} N'.format(i+1, force[i])
            f_format = np.append(f_format,x)
            i += i  
        f_format = "\n".join(f_format)
        
        #Plotting the legend
        plt.legend(('Beam',('Load position\nForce magnitude:\n{}'.format(f_format)),('Max. difl. = {:.2E} (m)'.format(np.max(y)))), loc = 'best')
    
    plt.show()
    