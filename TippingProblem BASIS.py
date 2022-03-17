
import numpy as np
import skfuzzy as fuzz

#STEP 1
########## INPUTS ########################
#Input Universe functions
service = np.arange(0,11,.1)
food    = np.arange(0,11,.1)
# Input Membership Functions
# Service
service_poor = fuzz.gaussmf(service ,0,1.5)
service_good = fuzz.gaussmf(service ,5,1.5)
service_excellent = fuzz.gaussmf(service ,10,1.5)
# Food
food_rancid = fuzz.trapmf(food , [0, 0, 1, 3])
food_delicious = fuzz.gaussmf(food ,10,1.5)

########## OUTPUT ########################
# loadprice
# Output Variables Domain
loadprice = np.arange(0,30,.1)
# Output  Membership Function 
loadprice_low  = fuzz.trimf(loadprice, [0, 5, 10])
loadprice_med = fuzz.trimf(loadprice, [10, 15, 25])
loadprice_high = fuzz.trimf(loadprice, [20, 25, 30])


#STEP 2
def food_category(food_in = 2):
    food_cat_rancid = fuzz.interp_membership(food,food_rancid,food_in) # Depends from Step 1
    food_cat_delicious = fuzz.interp_membership(food,food_delicious,food_in) # Depends form Step 1
    return dict(rancid = food_cat_rancid,delicious = food_cat_delicious)

def service_category(service_in = 4):
    service_cat_poor = fuzz.interp_membership(service,service_poor, service_in) # Depends from Step 1
    service_cat_good = fuzz.interp_membership(service,service_poor, service_in)
    service_cat_excellent = fuzz.interp_membership(service,service_excellent, service_in)
    return dict(poor = service_cat_poor, good = service_cat_good, excellent = service_cat_poor)

#Example input variables 
food_in = food_category(2.34)
service_in = service_category(1.03)
print ("For Service", service_in)
print ("For Food ",food_in)


#STEP 3
rule1 = np.fmax(service_in['poor'],food_in['rancid'])
rule2 = service_in['good']
rule3 = np.fmax(food_in['delicious'],service_in['excellent'])


#STEP 4
imp1 = np.fmin(rule1,loadprice_low)
imp2 = np.fmin(rule2,loadprice_med)
imp3 = np.fmin(rule3,loadprice_high)


#STEP 5
aggregate_membership = np.fmax(imp1, np.fmax(imp2,imp3))


#STEP 6
result_loadprice = fuzz.defuzz(loadprice, aggregate_membership , 'centroid')
print ("Load generated per cost Result", result_loadprice)




##NOTES
# OUTPUT will be 'Cost' correlating to 'Tip'
# INPUT 'whether on or off' in load curtailment correlating to service 











