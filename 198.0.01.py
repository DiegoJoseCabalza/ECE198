import matplotlib.pyplot as pl 
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control

#test functions

array0 = [1,2,3,4,5]
array1 = [6,7,8,9,10]
array2 = [11,12,13,14,15]
array = [array0, array1, array2]

    
#####

#Generate fuzzy membership functions
#copy paste x_qual, x_serv, x_tip from sample code for setup purposes
x_qual = np.arange(0, 11, 1)
x_serv = np.arange(0, 11, 1)
x_tip  = np.arange(0, 26, 1)

particle = fuzz.trimf(x_qual, [0,0,5])
velocity = fuzz.trimf(x_tip, [0,0,5])

            
