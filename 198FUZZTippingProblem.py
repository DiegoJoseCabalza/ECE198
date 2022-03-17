##based on tipping problem, will expand
#Tipping Problem is the only basis found that is best available
#Fuzzy Logic classifies output
#as for output (it defuzzes), need to see a value
# service and food labels arbitrary, need to see effect on arrays tlga
import numpy as np
import skfuzzy as fuzz

#STEP 1
########## INPUTS ########################
#Input Universe functions
## more sample arrays for testing. copy paste to substitute 
#[0,1,1,0,1,0,1,0,1,0]
#[1,1,0,0,1,1,0,0,1,0]
#[1,1,1,1,1,0,0,0,0,0]
service = np.array([0,1,1,0,1,0,1,0,1,0]) ##test array muna which will eventually represent and expand to 16x10 arrays(means more arrays)
food    = np.array([0,1,1,0,1,0,1,0,1,0])

#try to see difference between trimf and gaussmf(sigmf)
#effect of trimf, 1 to zero and vice-versa (like a Not Function)
#for now, trimf seems okay with the arrays
#the gaussmf i think shows the numerical equivalent of bell curve??
print("service", service) #arbitrary names service and food since based on Tipping problem
print("food", food)
# Input Membership Functions
# service
service_low = fuzz.trimf(service, [0, 0, 1]) ## kaya siguro nag flip kasi binilang yung 0 (0 became 1 and vice versa)
#service_med = fuzz.gaussmf(service ,5,1)
service_high = fuzz.trimf(service, [1, 1, 2])
print("service_low", service_low)
print("service_high", service_high)
# Food
#fuzz.trapmf(food , [0, 0, 1, 3])
food_low = fuzz.trimf(service, [0, 0, 1])
food_high = fuzz.trimf(service, [1, 1, 2])

print("food_low", food_low)
print("food_high", food_high)
########## OUTPUT ########################
# costload
# Output Variables Domain
costload = np.array([0,1,1,0,1,0,1,0,1,0])
# Output  Membership Function 
#costload_low  = fuzz.gaussmf(costload, 0,1)
costload_low  = fuzz.trimf(service, [0, 0, 1])

#costload_med = fuzz.trimf(costload, [5, 5, 15])

#costload_high = fuzz.gaussmf(costload, 10,1)
costload_high = fuzz.trimf(service, [1, 1, 2])

print("costload", costload_high)

##FIX Step 2 onwards so that it can cover more arrays and process arrays better

#STEP 2
def food_category(food_in = 1):
    #food_cat_low = fuzz.fuzzy_mult(food,food_low,food_in, 1) 
    #food_cat_high = fuzz.fuzzy_mult(food,food_high,food_in, 1)
    #fuzz.interp_universe(x, xmf, y) shows '[]'
    #fuzz.interp_membership(food,food_high,food_in)
    food_cat_low = fuzz.sigmf(food,food_low,food_in)  #will show zero for interp_membership
    food_cat_high = fuzz.sigmf(food,food_high,food_in) 

    return dict(low = food_cat_low, high = food_cat_high)

def service_category(service_in = 1):
    service_cat_low = fuzz.sigmf(service,service_low, service_in) # Depends from Step 1
    #service_cat_med = fuzz.interp_membership(service,service_med, service_in)
    service_cat_high = fuzz.sigmf(service,service_high, service_in)
    return dict(low = service_cat_low, high = service_cat_high)

#sigmf may actually be more needed than the interp.membership function
# service and food variables/categories will eventually be formally replaced. if only one is needed, can be adjusted naman

#Example input variables 
food_in = food_category(1) #2.34 and 1.03 were default from original problem
service_in = service_category(1) # set one muna for both categories as default
print ("For Service", service_in)
print ("For Food ",food_in)
##ayusin pa to since it kinda doesn't satisfy

#STEP 3
rule1 = np.fmax(service_in['low'],food_in['low'])
#rule2 = service_in['good']
rule3 = np.fmax(food_in['high'],service_in['high'])


#STEP 4
imp1 = np.fmin(rule1,costload_low)
#imp2 = np.fmin(rule2,costload_med)
imp3 = np.fmin(rule3,costload_high)


#STEP 5
aggregate_membership = np.fmax(imp1,imp3)


#STEP 6
result_costload1 = fuzz.defuzz(costload, aggregate_membership , 'som')
result_costload2 = fuzz.defuzz(costload, aggregate_membership , 'lom')
result_costload3 = fuzz.defuzz(costload, aggregate_membership , 'mom')
#‘centroid’: Centroid of area
#‘bisector’: bisector of area
#‘mom’ : mean of maximum
#‘som’ : min of maximum
#‘lom’ : max of maximum
#Load generated per cost Result???
#centroid yung pinalabas sa orig tipping problem
print ("costload1 min of max", result_costload1)
print ("costload2 max of max", result_costload2)
print ("costload3 mean of max", result_costload3)


##NOTES
# INPUT of arrays of 1s and 0s
# OUTPUT yung sa 'centroid' or 'bisector' need pa intindihin; another question is if neede
# input can now get arrays; next step yung pagkuha ng maraming arrays naman
# as mentioned previously, does this mean hardcoding 16x10 array











