#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:12:19 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    # MAIN 
    #
    # Interactive menu that allows user to use the code in all its functions
    #    
    # Input: Prompt, name of the file
    #
    # Output: Display statistics and Generate plots from the input data
    
from dataStatistics import dataStatistics
from dataLoad import dataLoad
from displayMenu import displayMenu
from dataPlot import dataPlot
from dataFilter import dataFilter
import numpy as np

# initializing variables
menuItems = (["Load data", "Filter data", "Display statistics", "Generate plots", "Quit"])
l_lim = 0
u_lim = 0
bactype = np.arange(1,5)
bacteria = 0
filtereddata = 0
dataLoaded = False      #To verify if the data is loaded
dataFiltered = False    #To verify if filters are applied

# Interactive menu starts
while True:
    choice = displayMenu(menuItems)
    
    #1. Data Load
    if choice == 1:
        while True:
            try:
                filename = str(input("Please enter the file name: \n")) 
                data = dataLoad(filename)
                dataLoaded = True
                break
            except OSError:
                print("\nNot Valid file name. Please try again.")
                
    #2. Filter Data
    elif choice == 2:
          if dataLoaded == False:
              print("Error: You have to choose 1. Load data before any other options")
          else:   
              OutputDataFilter=dataFilter(data) 
              filtereddata=OutputDataFilter[0]
              dataFiltered=OutputDataFilter[1]
              continue
                    
    #3. Statistic analysis               
    elif choice == 3:
        if dataLoaded == False:
                print("\nError: You have to choose 1. Load data before any other options\n")
        else:
            print('\nWould you like to calculate statistic for filtered or unfiltered data?')
            
            # Allows user to choose filtered or unfiltered data
            dataOptions = ("Filtered Data Statistics", "Unfiltered Data Statistics")
            menu1 = int(displayMenu(dataOptions))
            if (menu1 == 1) & (dataFiltered == False):
                print("\nError: You have to choose 2. Filter data before any other options\n")
                continue
            
            # Allows user to choose form a range of statistics 
            statistics=('Mean Temperature','Mean Growth rate','Std Temperature','Std Growth rate','Rows','Mean Cold Growth rate','Mean Hot Growth rate','Back')
            menu2 = int(displayMenu(statistics))
            if menu1 == 1:
                result = dataStatistics(filtereddata,statistics[menu2-1])
            if menu1 == 2:
                result = dataStatistics(data, statistics[menu2-1])
            if menu2 == 8:
                continue

    #4. Plot data                    
    elif choice == 4: 
        if dataLoaded == False:
            print("\nError: You have to choose 1. Load data before any other options\n")
        else: 
            # Allows user to choose filtered or unfiltered data
            print("\nWould you like to plot filtered or unfiltered data?")
            plotOptions =("Filtered Data Plot", "Unfiltered Data")
            plot = displayMenu(plotOptions)
            if plot == 1:
                if dataFiltered == False:
                    print("\nError: You have to choose 2. Filter data before plotting")
                else: 
                    dataFiltered == True
                    graph = dataPlot(filtereddata)
                    print("\nPlots available in the Plot window")
                    continue
            elif plot == 2:
                graph = dataPlot(data)
                print("\nPlots available in the Plot window\n")
                continue
            
    #5. Quit
    elif choice == 5:
        print("Adios amigos")
        break 

        
    
        
        
        
       
     
        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                    