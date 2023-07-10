#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 11:27:15 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

from displayMenu import displayMenu

    # DATAFILTER Filters the given data for chosen conditions, 
    # returns an updated set of data, wherein all data 
    # complies with the given conditions.
    #    
    # Input: data 
    #
    # Output: array with two elements: data (matrix of floats) 
    # dataFiltered (boolean variable)
    
def dataFilter(data):
    
    filteroptions = (['Apply Bacteria type filter', 'Apply Growth rate range filter', 'Do not apply filters'])
    option = displayMenu(filteroptions)
    
    # bacteria type
    if option == 1:
        bacteriaTypes = (['Salmonella enterica','Bacillus cereus', 'Listeria', 'Brochothrix thermosphacta'])
        bacteria = displayMenu(bacteriaTypes)
        filtereddata = (data[:,2] == bacteria)
        filtereddata=data[filtereddata]
        print("Data has been filtered for",bacteriaTypes[int(bacteria)-1])
        dataFiltered = True
        
    # growth rate
    elif option == 2:
        while True:            
            l_lim = float(input("Please enter a lower limit for the growth rate: ")) 
            u_lim = float(input("Please enter a upper limit for the growth rate: ")) 
            if l_lim > u_lim:
                print('\nLower limit cannot be higher than upper limit. Please try again')
                continue
            if ((l_lim != 0) or (u_lim != 0)):
                filtereddata = data[(data[:,1] >= l_lim) & (data[:,1] <= u_lim)] #Update data with a lower limt for growth rate
            dataFiltered = True
            break     
        
    # no filter
    elif option == 3:
        print('No filter applied.') 
        dataFiltered = False
        filtereddata=data

    return filtereddata, dataFiltered
