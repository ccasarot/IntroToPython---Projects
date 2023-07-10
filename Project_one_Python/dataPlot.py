#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 19:06:31 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    # dataPlot plots barchart and growth rate by temperature graph from
    # input data
    #    
    # Input: data file
    #
    # Output: graphs 

import numpy as np
import matplotlib.pyplot as plt

def dataPlot(data):
    
    #Plot 1
    
    #Data for datatype 1
    x1 = data[data[:,2]==1]
    y1 = data[data[:,2]==1]
    
    #Data for datatype 2
    x2 = data[data[:,2]==2]
    y2 = data[data[:,2]==2]
    
    #Data for datatype 3
    x3 = data[data[:,2]==3]
    y3 = data[data[:,2]==3]
    
    #Data for datatype 4
    x4 = data[data[:,2]==4]
    y4 = data[data[:,2]==4]
    
    #Bar chart
    x = ['Salmonella enterica', 'Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta'] #Each category of bacteria
    if (len(x1) != 0):                      #Check if data exist, if it doesn't dont plot
        plt.bar(x[0], len(x1), color="r")   #Plot bar graph of data
    if (len(x2) != 0):
        plt.bar(x[1], len(x2), color="b")
    if (len(x3) != 0):
        plt.bar(x[2], len(x3), color="y")
    if (len(x4) != 0):
        plt.bar(x[3], len(x4), color="g")
    plt.title("Number of bacteria")         #Set the title of the graph
    plt.xlabel("Data")                      #Set the x-axis label
    plt.ylabel("Amount of bacteria")        #Set the y-axis label
    plt.xticks(rotation=15)                 #Rotate labels to avoid overlap
    plt.xlim([-0.5, 3.5])                   #Set the limits of the x-axis
    plt.show()                              #Show the plots
    ###########################################################################
    
   #Second plot - Growth rate by Temperature
    
    #Defining coordinates
    temperatures = data[:,0]
    growthrate = data[:,1]
    
    indexforBacteria1T = np.where(data[:, 2] == 1)
    indexforBacteria1G = np.where(data[:, 2] == 1)
    x1 = temperatures[indexforBacteria1T]
    y1 = growthrate[indexforBacteria1G]
    
    indexforBacteria2T = np.where(data[:, 2] == 2)
    indexforBacteria2G = np.where(data[:, 2] == 2)
    x2 = temperatures[indexforBacteria2T]
    y2 = growthrate[indexforBacteria2G]
    
    indexforBacteria3T = np.where(data[:, 2] == 3)
    indexforBacteria3G = np.where(data[:, 2] == 3)
    x3 = temperatures[indexforBacteria3T]
    y3 = growthrate[indexforBacteria3G]
    
    indexforBacteria4T = np.where(data[:, 2] == 4)
    indexforBacteria4G = np.where(data[:, 2] == 4)
    x4 = temperatures[indexforBacteria4T]
    y4 = growthrate[indexforBacteria4G]
    
    plt.xlabel("Temperature") # Set the x-axis label
    plt.ylabel("Growth rate")
    plt.xlim([10, 60])
    plt.ylim([0,np.max(data[:,1])])
    
    #Ordering points
    if len(x1)==0:
        print('No Salmonella enterica found ')
    else:
        x1, y1 =zip(*sorted(zip(x1,y1)))
    if len(x2)==0:
        print('No  Bacillus cereus found ')
    else:
        x2, y2 =zip(*sorted(zip(x2,y2)))
    if len(x3)==0:
        print('No  Listeria found ')
    else:
        x3, y3 =zip(*sorted(zip(x3,y3)))
    if len(x4)==0:
        print('No  Brochothrix thermosphacta found ')
    else:
        x4, y4 =zip(*sorted(zip(x4,y4)))
    # Plot line graph of x and y   
    plt.plot(x1, y1, label ="Salmonella enterica") 
    plt.plot(x2, y2, label = "Bacillus cereus")
    plt.plot(x3, y3, label = "Listeria")
    plt.plot(x4, y4, label = "Brochothrix thermosphacta")
    
    #Layout
    plt.legend(loc ="lower center")
    plt.title('Growth rate by temperature')
    plt.show()