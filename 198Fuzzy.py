import numpy as np
import skfuzzy as fuzz
x = ([1,0,1,1,1,1,1,1,1], [1,0,1,1,1,1,1,1,1]) ##tried np.array (x) but doesn't work; hardcoded the arrays muna

#hardcode per array and consumption load given that scikit fuzzy functions are mostly math functions
# Progress:
# DUCost:working but not yet final
# SelfCost: pending but code snippet can be duplicated from DUCost
# Overcurtailment: working but not yet final
# Undercurtailment: working but not yet final
# OverEnergyLimit: working but not yet final


#set costs per kW here
DUcost = 10
SELFcost = 5

#capacity consumption; consX -> arrayX
cons01 = 320
cons02 = 200
cons03 = 80
cons04 = 84
cons05 = 100
cons06 = 160
cons07 = 100
cons08 = 60
cons09 = 200
cons10 = 40
cons11 = 40
cons12 = 72
cons13 = 140
cons14 = 80
cons15 = 40
cons16 = 180
cons17 = 180
cons18 = 160
cons19 = 60
cons20 = 50
consT = 2346


#self generated energy for each load in kW 
self = 0

array01 = np.array([0,0,0,0,1,1,1,0,0,0,1,1,0,0,0,0])
array02 = np.array([0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0])
array03 = np.array([1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,0])
array04 = np.array([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
array05 = np.array([0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0])
array06 = np.array([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0])
array07 = np.array([0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,1])
array08 = np.array([0,0,0,0,1,1,0,1,0,1,1,0,0,0,0,0])
array09 = np.array([0,1,1,0,0,1,0,1,0,0,1,1,0,0,0,0])
array10 = np.array([1,0,0,1,0,1,0,0,0,0,1,1,1,0,0,1])


#####    DU SUPPLIED COST     #####

#fuzz.sigmf and fuzz.trimf is applied based on the Tipping Problem
Farray01 = fuzz.sigmf(array01, fuzz.trimf(array01, [0, 0, 1]), 1)
Farray02 = fuzz.sigmf(array02, fuzz.trimf(array02, [0, 0, 1]), 1)
Farray03 = fuzz.sigmf(array03, fuzz.trimf(array03, [0, 0, 1]), 1)
Farray04 = fuzz.sigmf(array04, fuzz.trimf(array04, [0, 0, 1]), 1)
Farray05 = fuzz.sigmf(array05, fuzz.trimf(array05, [0, 0, 1]), 1)
Farray06 = fuzz.sigmf(array06, fuzz.trimf(array06, [0, 0, 1]), 1)
Farray07 = fuzz.sigmf(array07, fuzz.trimf(array07, [0, 0, 1]), 1)
Farray08 = fuzz.sigmf(array08, fuzz.trimf(array08, [0, 0, 1]), 1)
Farray09 = fuzz.sigmf(array09, fuzz.trimf(array09, [0, 0, 1]), 1)
Farray10 = fuzz.sigmf(array10, fuzz.trimf(array10, [0, 0, 1]), 1)


# 0's become 0.26894; 1's become 0.73106
#print('Farray01',Farray01) #use this line and sub the numbers for debugging

#Calculate DU
#muliply capacity consumption value by the fuzzified array
DU01 = np.multiply(cons01, Farray01)
DU02 = np.multiply(cons02, Farray02)
DU03 = np.multiply(cons03, Farray03)
DU04 = np.multiply(cons04, Farray04)
DU05 = np.multiply(cons05, Farray05)
DU06 = np.multiply(cons06, Farray06)
DU07 = np.multiply(cons07, Farray07)
DU08 = np.multiply(cons08, Farray08)
DU09 = np.multiply(cons09, Farray09)
DU10 = np.multiply(cons10, Farray10)

#use print('DUxx', DUxx) and uncomment for debugging
#print('DU01 Array', DU01)

print('DU01 Max and Min:', np.nanmax(DU01), np.nanmin(DU01)) #gets the max(correlates to 1) and min(correlates to 0) values of the array
print('DU02 Max and Min:', np.nanmax(DU02), np.nanmin(DU02))
print('DU03 Max and Min:', np.nanmax(DU03), np.nanmin(DU03))
print('DU04 Max and Min:', np.nanmax(DU04), np.nanmin(DU04))
print('DU05 Max and Min:', np.nanmax(DU05), np.nanmin(DU05))
print('DU06 Max and Min:', np.nanmax(DU06), np.nanmin(DU06))
print('DU07 Max and Min:', np.nanmax(DU07), np.nanmin(DU07))
print('DU08 Max and Min:', np.nanmax(DU08), np.nanmin(DU08))
print('DU09 Max and Min:', np.nanmax(DU09), np.nanmin(DU09))
print('DU10 Max and Min:', np.nanmax(DU10), np.nanmin(DU10))

DUTotal = np.nanmax(DU01)+np.nanmax(DU02)+np.nanmax(DU03)+np.nanmax(DU04)+np.nanmax(DU05)+np.nanmax(DU06)+np.nanmax(DU07)+np.nanmax(DU08)+np.nanmax(DU09)+np.nanmax(DU10)
print('DU Max Total', DUTotal)


#####    CURTAILMENT COST AND OVERCURTAILMENT     #####

Fcons01 = np.nanmax(DU01) #fuzzified consumption values in case if needed
Fcons02 = np.nanmax(DU02)
Fcons03 = np.nanmax(DU03)
Fcons04 = np.nanmax(DU04)
Fcons05 = np.nanmax(DU05)
Fcons06 = np.nanmax(DU06)
Fcons07 = np.nanmax(DU07)
Fcons08 = np.nanmax(DU08)
Fcons09 = np.nanmax(DU09)
Fcons10 = np.nanmax(DU10)

#arbitrary penalty values
penaltyvalue = 1

#limit for each TS
TSlimit01 = 110
TSlimit02 = 220
TSlimit03 = 455
TSlimit04 = 680
TSlimit05 = 770
TSlimit06 = 800
TSlimit07 = 750
TSlimit08 = 640
TSlimit09 = 590
TSlimit10 = 610
TSlimit11 = 660
TSlimit12 = 680
TSlimit13 = 570
TSlimit14 = 410
TSlimit15 = 230
TSlimit16 = 135

#minimum off time per load
minlimit01 = 2
minlimit02 = 2
minlimit03 = 2
minlimit04 = 2
minlimit05 = 2
minlimit06 = 2
minlimit07 = 1
minlimit08 = 1
minlimit09 = 1
minlimit10 = 1

#maximum off time per load
maxlimit01 = 4
maxlimit02 = 4
maxlimit03 = 4
maxlimit04 = 4
maxlimit05 = 4
maxlimit06 = 4
maxlimit07 = 3
maxlimit08 = 3
maxlimit09 = 3
maxlimit10 = 4

consumption = [cons01,cons02,cons03,cons04,cons05,cons06,cons07,cons08,cons09,cons10]

#Fconsumption shows the array of fuzzifed consumption values
Fconsumption = [np.nanmax(DU01),np.nanmax(DU02),np.nanmax(DU03),np.nanmax(DU04),np.nanmax(DU05)]

#note the format: arrayXX = [TS01,TS02,TS03,TS04,TS05,TS06,TS07,TS08,TS09,TS10,TS11,TS12,TS13,TS14,TS15,TS16]

TS01 = (array01[0],array02[0],array03[0],array04[0],array05[0],array06[0],array07[0],array08[0],array09[0],array10[0])
TS02 = (array01[1],array02[1],array03[1],array04[1],array05[1],array06[1],array07[1],array08[1],array09[1],array10[1])
TS03 = (array01[2],array02[2],array03[2],array04[2],array05[2],array06[2],array07[2],array08[2],array09[2],array10[2])
TS04 = (array01[3],array02[3],array03[3],array04[3],array05[3],array06[3],array07[3],array08[3],array09[3],array10[3])
TS05 = (array01[4],array02[4],array03[4],array04[4],array05[4],array06[4],array07[4],array08[4],array09[4],array10[4])
TS06 = (array01[5],array02[5],array03[5],array04[5],array05[5],array06[5],array07[5],array08[5],array09[5],array10[5])
TS07 = (array01[6],array02[6],array03[6],array04[6],array05[6],array06[6],array07[6],array08[6],array09[6],array10[6])
TS08 = (array01[7],array02[7],array03[7],array04[7],array05[7],array06[7],array07[7],array08[7],array09[7],array10[7])
TS09 = (array01[8],array02[8],array03[8],array04[8],array05[8],array06[8],array07[8],array08[8],array09[8],array10[8])
TS10 = (array01[9],array02[9],array03[9],array04[9],array05[9],array06[9],array07[9],array08[9],array09[9],array10[9])
TS11 = (array01[10],array02[10],array03[10],array04[10],array05[10],array06[10],array07[10],array08[10],array09[10],array10[10])
TS12 = (array01[11],array02[11],array03[11],array04[11],array05[11],array06[11],array07[11],array08[11],array09[11],array10[11])
TS13 = (array01[12],array02[12],array03[12],array04[12],array05[12],array06[12],array07[12],array08[12],array09[12],array10[12])
TS14 = (array01[13],array02[13],array03[13],array04[13],array05[13],array06[13],array07[13],array08[13],array09[13],array10[13])
TS15 = (array01[14],array02[14],array03[14],array04[14],array05[14],array06[14],array07[14],array08[14],array09[14],array10[14])
TS16 = (array01[15],array02[15],array03[15],array04[15],array05[15],array06[15],array07[15],array08[15],array09[15],array10[15])

##     OVERENERGYLIMIT     ##
OEtotalpenalty = 0
#print('TS01', np.sum(np.multiply(TS01,consumption))) use line for debugging
if np.sum(np.multiply(TS01,consumption)) > TSlimit01:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS02,consumption)) > TSlimit02:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS03,consumption)) > TSlimit03:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS04,consumption)) > TSlimit04:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS05,consumption)) > TSlimit05:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS06,consumption)) > TSlimit06:
    OEtotalpenalty += 1
    
if np.sum(np.multiply(TS07,consumption)) > TSlimit07:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS08,consumption)) > TSlimit08:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS09,consumption)) > TSlimit09:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS10,consumption)) > TSlimit10:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS11,consumption)) > TSlimit11:
    OEtotalpenalty += 1
    
if np.sum(np.multiply(TS12,consumption)) > TSlimit12:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS13,consumption)) > TSlimit13:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS14,consumption)) > TSlimit14:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS15,consumption)) > TSlimit15:
    OEtotalpenalty += 1

if np.sum(np.multiply(TS16,consumption)) > TSlimit16:
    OEtotalpenalty += 1    

OEFinalTotalPenalty = OEtotalpenalty*penaltyvalue

print('totalpenalty from OverEnergyLimit', OEFinalTotalPenalty)


##     OVERCURTAILMENT     ##
OCtotalpenalty = 0

if np.count_nonzero(array01) > maxlimit01:
    OCtotalpenalty += 1
    
if np.count_nonzero(array02) > maxlimit02:
    OCtotalpenalty += 1
    
if np.count_nonzero(array03) > maxlimit03:
    OCtotalpenalty += 1
    
if np.count_nonzero(array04) > maxlimit04:
    OCtotalpenalty += 1
    
if np.count_nonzero(array05) > maxlimit05:
    OCtotalpenalty += 1

if np.count_nonzero(array06) > maxlimit06:
    OCtotalpenalty += 1

if np.count_nonzero(array07) > maxlimit07:
    OCtotalpenalty += 1

if np.count_nonzero(array08) > maxlimit08:
    OCtotalpenalty += 1

if np.count_nonzero(array09) > maxlimit09:
    OCtotalpenalty += 1

if np.count_nonzero(array10) > maxlimit10:
    OCtotalpenalty += 1

OCFinalTotalPenalty = OCtotalpenalty*penaltyvalue

print('totalpenalty from OverCurtailment', OCFinalTotalPenalty)

##     UNDERCURTAILMENT     ##
UCtotalpenalty = 0

if np.count_nonzero(array01) < minlimit01:
    UCtotalpenalty += 1
    
if np.count_nonzero(array02) < minlimit02:
    UCtotalpenalty += 1
    
if np.count_nonzero(array03) < minlimit03:
    UCtotalpenalty += 1
    
if np.count_nonzero(array04) < minlimit04:
    UCtotalpenalty += 1
    
if np.count_nonzero(array05) < minlimit05:
    UCtotalpenalty += 1

if np.count_nonzero(array06) < minlimit06:
    UCtotalpenalty += 1

if np.count_nonzero(array07) < minlimit07:
    UCtotalpenalty += 1

if np.count_nonzero(array08) < minlimit08:
    UCtotalpenalty += 1

if np.count_nonzero(array09) < minlimit09:
    UCtotalpenalty += 1

if np.count_nonzero(array10) < minlimit10:
    UCtotalpenalty += 1

UCFinalTotalPenalty = UCtotalpenalty*penaltyvalue
print('totalpenalty from OverCurtailment', UCFinalTotalPenalty)


#count number of 1s (hours) per array which is number 
print('count of 1s in array01: ', np.count_nonzero(array01))
print('count of 1s in array02: ', np.count_nonzero(array02))
print('count of 1s in array03: ', np.count_nonzero(array03))
print('count of 1s in array04: ', np.count_nonzero(array04))
print('count of 1s in array05: ', np.count_nonzero(array05))
print('count of 1s in array06: ', np.count_nonzero(array06))
print('count of 1s in array07: ', np.count_nonzero(array07))
print('count of 1s in array08: ', np.count_nonzero(array08))
print('count of 1s in array09: ', np.count_nonzero(array09))
print('count of 1s in array10: ', np.count_nonzero(array10))


OF = DUTotal + OEFinalTotalPenalty + OCFinalTotalPenalty + UCFinalTotalPenalty
print('OF', OF)






#This defuzz part is based on the last part of tipping problem, but unviable when I applied it mid code in DU calculation

#fuzz.defuzz(x, mfx, mode) -> modes: 'centroid', 'bisector', 'mom', 'som', 'lom'
#fuzz.defuzzify.centroid(x, mfx)
#FDU01 = fuzz.defuzz(DU01, acons01, 'centroid')
#FDU02 = fuzz.defuzzify.centroid(array02, DU02)
#print('defuzzed DU01', FDU01)
#print('defuzzed DU02', FDU02)

#process done on Tipping Problem from the BASIS code can be possibly applied on the value of OF which can classify how high or how low









    
