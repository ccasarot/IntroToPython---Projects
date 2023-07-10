#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:17:37 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

    # dataStatistics 
    #
    # Input: data, string of statistic to be calculated
    #
    # Output: description of the statistic chosen by user and its calculation
    
import numpy as np
def dataStatistics(data, statistic):

    statistics_options=np.array(["Mean Temperature", "Mean Growth rate",
                                 "Std Temperature", "Std Growth rate",
                                 "Rows", "Mean Cold Growth rate",
                                 "Mean Hot Growth rate", "Back"])
    Temperature = data[:,0]
    Growthrate = data[:,1]
    if statistic == statistics_options[0]:
        result=np.mean(Temperature)
        print("\nThe Mean Temperature is:", str(result))
        print("\nDESCRIPTION: the mean temperature is the sum of all the temperatures considered in the data, divided by the total number of temperatures considered")

    elif statistic==statistics_options[1]:
        
        result=np.mean(Growthrate)    
        print("\nThe Mean Growth rate is:", str(result))
        print("\nDESCRIPTION: the mean growth rate is the sum of all the growth rates considered in the data, divided by the total number of growth rates considered")
        
    elif statistic==statistics_options[2]:
        
        result=np.std(Temperature)
        print("\nThe Std Temperature is:", str(result))
        print("\nDESCRIPTION: the standard deviation of temperature is the square root of the average of the squared deviations from the mean, \
                  i.e., std = sqrt(mean(x)), where x = abs(data - data.mean())**2.")
        
    elif statistic==statistics_options[3]:
     
        result=np.std(Growthrate)
        print("\nThe Std Growth rate is:", str(result))
        print("\nDESCRIPTION: The standard deviation of growth rate is the square root of the average of the squared deviations from the mean, i.e., std = sqrt(mean(x)), where x = abs(data - data.mean())**2.")
        
    elif statistic==statistics_options[4]:
        result= np.shape(data)[0]
        print("\nThe number of rows is:", str(result))
        print("\nDESCRIPTION: this is the number of rows in the data")
        
    elif statistic==statistics_options[5]: #when Temperature<20
        count=0
        for rows in data:
            if rows[0]>20:
                data=np.delete(data, count,0)
                count= count-1
            count=count+1
        
        
        result=np.mean(Growthrate)
        print("\nThe Mean Cold Growth rate is:", str(result))
        print("\nDESCRIPTION: the mean cold growth rate is the sum of all the growth rates considered in the data when tempearure is less than 20 degrees, divided by the total number of growth rates considered")
        
    elif statistic==statistics_options[6]: #when temperature>50
        count=0
        for rows in data:
            if rows[0]<50:
                data=np.delete(data, count,0)
                count= count-1
            count=count+1
    
        result=np.mean(Growthrate)
        print("\nThe Mean Hot Growth rate is:", str(result))
        print("\nDESCRIPTION: the mean hot growth rate is the sum of all the growth rates considered in the data when tempearure is grater than 50 degrees, divided by the total number of growth rates considered") 
    elif statistic==statistics_options[7]:
        result = print('Initializing menu')
    
    return result