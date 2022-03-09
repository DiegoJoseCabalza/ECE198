import matplotlib.pyplot as pl 
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control

#status
# position function: x
# velocity function: x
# objective function: x


#test functions

array0 = [0,1,2]
array1 = [1,2,3]
array2 = [4,5,6]
array = [array0, array1, array2]

##np.arange can have 100 iterations for sample but set to 10-11 first
##np.array can set specific values
x = np.arange(11)
mfx1 = fuzz.trimf(x, array0)
mfx2 = fuzz.trimf(x, array1)
#test adding arrays
print(x)
print(mfx1)
print(mfx2)
sum = mfx1 + mfx2
print(sum)
#####
A = np.array([1,2,3,4,5,6,7,8,9,10])
print(A)
nfx1 = fuzz.trimf(A, array0)
print(nfx1)
#####
## try repeat test3 but for dimensions, particles, velocity, and position

# Generate universe variables
# * Quality and service on subjective ranges [0, 10]
x_dimension = np.arange(0, 5, 1)
x_particle = np.arange(0, 10, 1)
x_velocity = np.arange(0, 10, 1)

x_position = np.arange(0, 10, 1)


# Generate fuzzy membership functions
dim_lo = fuzz.trimf(x_dimension, [0, 0, 5])
dim_hi = fuzz.trimf(x_dimension, [5, 10, 10])
part_lo = fuzz.trimf(x_particle, [0, 0, 5])
part_hi = fuzz.trimf(x_particle, [5, 10, 10])
vel_lo = fuzz.trimf(x_velocity, [0, 0, 5])
vel_hi = fuzz.trimf(x_velocity, [5, 10, 10])
pos_lo = fuzz.trimf(x_position, [0, 0, 5])
pos_hi = fuzz.trimf(x_position, [5, 10, 10])

#based from testcode, cant show plot for whatever reason
#attempts in printing the output
fig, (ax0) = pl.subplots(nrows=3, figsize=(8, 9))
ax0.plot(x_dimension, dim_lo, linewidth=1.5, label='A')
ax0.plot(x_dimension, dim_md, linewidth=1.5, label='B')
ax0.set_title('dimension')
ax0.legend()
print(dim_lo)

#set arbitrary values
c1 = 1
c2 = 2
w = 3
particles = 1
dimensions = 1
# define objective functions


#y = np.arange(51)


#velocity computation, closer look on scikit functions
#check fuzzymath functions for pbestpos, bestcost, and position
def _compute_velocity(a,c1,c2,w):
    for i in range(x):                  
        for j in range(y):
            [c1*np.random.uniform(low=0.0, high=1.0)*pbestpos]-[c1*np.random.uniform(low=0.0, high=1.0)*position] + \
            [c2*np.random.uniform(low=0.0, high=1.0)*bestcost]-[c2*np.random.uniform(low=0.0, high=1.0)*position]
    return 

#compute position, kulang pa
#skfuzzy.sigmoid(x, power[, split])
#skfuzzy.sigmf(x, b, c) or skfuzzy.trimf(x, abc) *note skfuzzy -> fuzz
##fix pa

#def _compute_position(a):
#
#    for i in range(x):
#        for j in range(y):
#            if fuzz.sigmoid(x, power[x, split]) < np.random.uniform(low=0.0, high=1.0): 
#            else
#
#    return 

# fuzz.fuzzymath.fuzzy_compare(q)

# Compute current cost

# Compute personal best cost

# 
#
#
