#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:44:29 2022

@author: Marica Sudano s225578 - Christian Casarotto s223302
"""

# dataLoad cleans the data removing the invalid rows from the matrix
#
# imput: Name of the file cointaing the data. The data is a Nx3 matrix where
#        the first column is the Temperature, the second the Growth Rate and
#        the third is the Bacteria id
# output: A matrix where the invalid rows of data are removed, with respect
#         to given bounddary conditions
#         It also prints to screen an error message, reporting the reason 
#         of the error and the row where it occurred

import numpy as np

def dataLoad(filename):
    print('\n')
    
    # loading the file and creating arrays for later phases
    filein = np.loadtxt(filename) 
    selection=np.zeros(len(filein), dtype=bool) 
    generalErrorMessage=np.array(['Temperature out of boundaries. ', 'Growth Rate negative. ', 'Wrong Bacteria ID.'])
    
    # verification of the boundary conditions
    for i in range(len(filein)): 
        condition=([(filein[i,0]>10) & (filein[i,0]<60),(filein[i,1]>0),(filein[i,2]==1 or filein[i,2]==2 or filein[i,2]==3 or filein[i,2]==4)])
        selection[i]=np.all(condition) 

        # display the error message where conditions are not verified
        if selection[i]==False:
            message=''.join(generalErrorMessage[np.invert(condition)])
            print("Line",i,"excluded",message)
    
    data=filein[selection]
    return data

