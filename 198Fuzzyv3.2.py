import numpy as np
import skfuzzy as fuzz
x = ([1,0,1,1,1,1,1,1,1], [1,0,1,1,1,1,1,1,1]) ##tried np.array (x) but doesn't work; hardcoded the arrays muna

#hardcode per array and consumption load given that scikit fuzzy functions are mostly math functions
# Progress:
# DUCost: OK
# SelfCost: OK; based from DUCost
# Overcurtailment: OK
# Undercurtailment: OK
# RequiredCurtailment : OK
# ExcessCurtailment : OK

#capacity consumption; consX -> arrayX
C01 = 320
C02 = 200
C03 = 80
C04 = 84
C05 = 100
C06 = 160
C07 = 100
C08 = 60
C09 = 200
C10 = 40
C11 = 40
C12 = 72
C13 = 140
C14 = 80
C15 = 40
C16 = 180
C17 = 180
C18 = 160
C19 = 60
C20 = 50

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
array11 = np.array([0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0])
array12 = np.array([0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
array13 = np.array([0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0])
array14 = np.array([0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0])
array15 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
array16 = np.array([0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0])
array17 = np.array([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
array18 = np.array([0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,0])
array19 = np.array([0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0])
array20 = np.array([0,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0])

#####    DU SUPPLIED COST AND SELF SUPPLIED COST     #####

#fuzz.sigmoid applied on the arrays to apply Fuzzy logic
#skfuzzy.sigmoid(x, power, split=0.5)
#x : ndarray; Input vector or image array. Should be pre-normalized to range [0, 1]
#p : float; Power of the intensification (p > 0). Experiment with small, decimal values and increase as necessary.
## changing the value of p affects the values of array in performing fuzz.sigmoid, a form of sensitivity analysis
#split : floatThreshold for intensification. Values above split will be intensified,
#while values below split will be deintensified. Note range for split is (0, 1). Default of 0.5 is reasonable for many well-exposed images
##split value set to default 0.5

#fuzz.sigmf(x, b, c)

Farray01 = fuzz.sigmoid(array01, 2, split=0.5)
Farray02 = fuzz.sigmoid(array02, 2, split=0.5)
Farray03 = fuzz.sigmoid(array03, 2, split=0.5)
Farray04 = fuzz.sigmoid(array04, 2, split=0.5)
Farray05 = fuzz.sigmoid(array05, 2, split=0.5)
Farray06 = fuzz.sigmoid(array06, 2, split=0.5)
Farray07 = fuzz.sigmoid(array07, 2, split=0.5)
Farray08 = fuzz.sigmoid(array08, 2, split=0.5)
Farray09 = fuzz.sigmoid(array09, 2, split=0.5)
Farray10 = fuzz.sigmoid(array10, 2, split=0.5)
Farray11 = fuzz.sigmoid(array11, 2, split=0.5)
Farray12 = fuzz.sigmoid(array12, 2, split=0.5)
Farray13 = fuzz.sigmoid(array13, 2, split=0.5)
Farray14 = fuzz.sigmoid(array14, 2, split=0.5)
Farray15 = fuzz.sigmoid(array15, 2, split=0.5)
Farray16 = fuzz.sigmoid(array16, 2, split=0.5)
Farray17 = fuzz.sigmoid(array17, 2, split=0.5)
Farray18 = fuzz.sigmoid(array18, 2, split=0.5)
Farray19 = fuzz.sigmoid(array19, 2, split=0.5)
Farray20 = fuzz.sigmoid(array20, 2, split=0.5)
# 0's become 0.26894; 1's become 0.73106
#print('Farray01',Farray01) #use this line and sub the numbers for debugging
#Calculate DU Load
#muliply capacity consumption value by the fuzzified array
DU01 = np.multiply((C01-self), Farray01)
DU02 = np.multiply((C02-self), Farray02)
DU03 = np.multiply((C03-self), Farray03)
DU04 = np.multiply((C04-self), Farray04)
DU05 = np.multiply((C05-self), Farray05)
DU06 = np.multiply((C06-self), Farray06)
DU07 = np.multiply((C07-self), Farray07)
DU08 = np.multiply((C08-self), Farray08)
DU09 = np.multiply((C09-self), Farray09)
DU10 = np.multiply((C10-self), Farray10)
DU11 = np.multiply((C11-self), Farray11)
DU12 = np.multiply((C12-self), Farray12)
DU13 = np.multiply((C13-self), Farray13)
DU14 = np.multiply((C14-self), Farray14)
DU15 = np.multiply((C15-self), Farray15)
DU16 = np.multiply((C16-self), Farray16)
DU17 = np.multiply((C17-self), Farray17)
DU18 = np.multiply((C18-self), Farray18)
DU19 = np.multiply((C19-self), Farray19)
DU20 = np.multiply((C20-self), Farray20)

DFU01 = fuzz.defuzz(DU01, fuzz.trimf(DU01, [0, 1, 1]), 'lom')
DFU02 = fuzz.defuzz(DU02, fuzz.trimf(DU02, [0, 1, 1]), 'lom')
DFU03 = fuzz.defuzz(DU03, fuzz.trimf(DU03, [0, 1, 1]), 'lom')
DFU04 = fuzz.defuzz(DU04, fuzz.trimf(DU04, [0, 1, 1]), 'lom')
DFU05 = fuzz.defuzz(DU05, fuzz.trimf(DU05, [0, 1, 1]), 'lom')
DFU06 = fuzz.defuzz(DU06, fuzz.trimf(DU06, [0, 1, 1]), 'lom')
DFU07 = fuzz.defuzz(DU07, fuzz.trimf(DU07, [0, 1, 1]), 'lom')
DFU08 = fuzz.defuzz(DU08, fuzz.trimf(DU08, [0, 1, 1]), 'lom')
DFU09 = fuzz.defuzz(DU09, fuzz.trimf(DU09, [0, 1, 1]), 'lom')
DFU10 = fuzz.defuzz(DU10, fuzz.trimf(DU10, [0, 1, 1]), 'lom')
DFU11 = fuzz.defuzz(DU11, fuzz.trimf(DU11, [0, 1, 1]), 'lom')
DFU12 = fuzz.defuzz(DU12, fuzz.trimf(DU12, [0, 1, 1]), 'lom')
DFU13 = fuzz.defuzz(DU13, fuzz.trimf(DU13, [0, 1, 1]), 'lom')
DFU14 = fuzz.defuzz(DU14, fuzz.trimf(DU14, [0, 1, 1]), 'lom')
DFU15 = fuzz.defuzz(DU15, fuzz.trimf(DU15, [0, 1, 1]), 'lom')
DFU16 = fuzz.defuzz(DU16, fuzz.trimf(DU16, [0, 1, 1]), 'lom')
DFU17 = fuzz.defuzz(DU17, fuzz.trimf(DU17, [0, 1, 1]), 'lom')
DFU18 = fuzz.defuzz(DU18, fuzz.trimf(DU18, [0, 1, 1]), 'lom')
DFU19 = fuzz.defuzz(DU19, fuzz.trimf(DU19, [0, 1, 1]), 'lom')
DFU20 = fuzz.defuzz(DU20, fuzz.trimf(DU20, [0, 1, 1]), 'lom')

#use print('DUxx', DUxx) and uncomment for debugging; shows new array
#print('DU01 Array', DU01)

print('DU01: ', DFU01) #gets the value that(correlates to 1) multiplied by the DU Load
print('DU02: ', DFU02)
print('DU03: ', DFU03)
print('DU04: ', DFU04)
print('DU05: ', DFU05)
print('DU06: ', DFU06)
print('DU07: ', DFU07)
print('DU08: ', DFU08)
print('DU09: ', DFU09)
print('DU10: ', DFU10)
print('DU11: ', DFU11)
print('DU12: ', DFU12)
print('DU13: ', DFU13)
print('DU14: ', DFU14)
print('DU15: ', DFU15)
print('DU16: ', DFU16)
print('DU17: ', DFU17)
print('DU18: ', DFU18)
print('DU19: ', DFU19)
print('DU20: ', DFU20)

DUTotal = DFU01+DFU02+DFU03+DFU04+DFU05+DFU06+DFU07+DFU08+DFU09+DFU10+DFU11+DFU12+DFU13+DFU14+DFU15+DFU16+DFU17+DFU18+DFU19+DFU20
print('DU Max Total', DUTotal)

#Calculate Self Load
SL01 = np.multiply(self, Farray01)
SL02 = np.multiply(self, Farray02)
SL03 = np.multiply(self, Farray03)
SL04 = np.multiply(self, Farray04)
SL05 = np.multiply(self, Farray05)
SL06 = np.multiply(self, Farray06)
SL07 = np.multiply(self, Farray07)
SL08 = np.multiply(self, Farray08)
SL09 = np.multiply(self, Farray09)
SL10 = np.multiply(self, Farray10)
SL11 = np.multiply(self, Farray11)
SL12 = np.multiply(self, Farray12)
SL13 = np.multiply(self, Farray13)
SL14 = np.multiply(self, Farray14)
SL15 = np.multiply(self, Farray15)
SL16 = np.multiply(self, Farray16)
SL17 = np.multiply(self, Farray17)
SL18 = np.multiply(self, Farray18)
SL19 = np.multiply(self, Farray19)
SL20 = np.multiply(self, Farray20)

#print('self load array01', SL01)
SFU01 = fuzz.defuzz(SL01, fuzz.trimf(SL01, [0, 1, 1]), 'lom')
SFU02 = fuzz.defuzz(SL02, fuzz.trimf(SL02, [0, 1, 1]), 'lom')
SFU03 = fuzz.defuzz(SL03, fuzz.trimf(SL03, [0, 1, 1]), 'lom')
SFU04 = fuzz.defuzz(SL04, fuzz.trimf(SL04, [0, 1, 1]), 'lom')
SFU05 = fuzz.defuzz(SL05, fuzz.trimf(SL05, [0, 1, 1]), 'lom')
SFU06 = fuzz.defuzz(SL06, fuzz.trimf(SL06, [0, 1, 1]), 'lom')
SFU07 = fuzz.defuzz(SL07, fuzz.trimf(SL07, [0, 1, 1]), 'lom')
SFU08 = fuzz.defuzz(SL08, fuzz.trimf(SL08, [0, 1, 1]), 'lom')
SFU09 = fuzz.defuzz(SL09, fuzz.trimf(SL09, [0, 1, 1]), 'lom')
SFU10 = fuzz.defuzz(SL10, fuzz.trimf(SL10, [0, 1, 1]), 'lom')
SFU11 = fuzz.defuzz(SL11, fuzz.trimf(SL11, [0, 1, 1]), 'lom')
SFU12 = fuzz.defuzz(SL12, fuzz.trimf(SL12, [0, 1, 1]), 'lom')
SFU13 = fuzz.defuzz(SL13, fuzz.trimf(SL13, [0, 1, 1]), 'lom')
SFU14 = fuzz.defuzz(SL14, fuzz.trimf(SL14, [0, 1, 1]), 'lom')
SFU15 = fuzz.defuzz(SL15, fuzz.trimf(SL15, [0, 1, 1]), 'lom')
SFU16 = fuzz.defuzz(SL16, fuzz.trimf(SL16, [0, 1, 1]), 'lom')
SFU17 = fuzz.defuzz(SL17, fuzz.trimf(SL17, [0, 1, 1]), 'lom')
SFU18 = fuzz.defuzz(SL18, fuzz.trimf(SL18, [0, 1, 1]), 'lom')
SFU19 = fuzz.defuzz(SL19, fuzz.trimf(SL19, [0, 1, 1]), 'lom')
SFU20 = fuzz.defuzz(SL20, fuzz.trimf(SL20, [0, 1, 1]), 'lom')

print('Self Load01', SFU01)
print('Self Load02', SFU02)
print('Self Load03', SFU03)
print('Self Load04', SFU04)
print('Self Load05', SFU05)
print('Self Load06', SFU06)
print('Self Load07', SFU07)
print('Self Load08', SFU08)
print('Self Load09', SFU09)
print('Self Load10', SFU10)

SelfLoadTotal = SFU01+SFU02+SFU03+SFU04+SFU05+SFU06+SFU07+SFU08+SFU09+SFU10+SFU11+SFU12+SFU13+SFU14+SFU15+SFU16+SFU17+SFU18+SFU19+SFU20
print('Self Load Total', SelfLoadTotal)

#####    CURTAILMENT COST AND OVERCURTAILMENT     #####

#arbitrary penalty values
penaltyvalue = 1

#limit for each TS
TSlimit01 = 110
TSlimit02 = 230
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
minon01 = 2
minon02 = 2
minon03 = 2
minon04 = 2
minon05 = 2
minon06 = 2
minon07 = 1
minon08 = 1
minon09 = 1
minon10 = 1
minon11 = 1
minon12 = 3
minon13 = 3
minon14 = 3
minon15 = 3
minon16 = 3
minon17 = 2
minon18 = 2
minon19 = 2
minon20 = 2

#maximum off time per load
maxoff01 = 4
maxoff02 = 4
maxoff03 = 4
maxoff04 = 4
maxoff05 = 4
maxoff06 = 4
maxoff07 = 3
maxoff08 = 3
maxoff09 = 3
maxoff10 = 4
maxoff11 = 3
maxoff12 = 3
maxoff13 = 4
maxoff14 = 3
maxoff15 = 3
maxoff16 = 3
maxoff17 = 4
maxoff18 = 4
maxoff19 = 4
maxoff20 = 4

consumption = [C01-self,C02-self,C03-self,C04-self,C05-self,C06-self,C07-self,C08-self,C09-self,C10-self,C11-self,C12-self,C13-self,C14-self,C15-self,C16-self,C17-self,C18-self,C19-self,C20-self]

#Fconsumption shows the array of fuzzifed consumption values
Fconsumption = [DFU01-self,DFU02-self,DFU03-self,DFU04-self,DFU05-self,DFU06-self,DFU07-self,DFU08-self,DFU09-self,DFU10-self,DFU11-self,DFU12-self,DFU13-self,DFU14-self,DFU15-self,DFU16-self,DFU17-self,DFU18-self,DFU19-self,DFU20-self]
#print('Fconsumption',Fconsumption)
#note the format: arrayXX = [TS01,TS02,TS03,TS04,TS05,TS06,TS07,TS08,TS09,TS10,TS11,TS12,TS13,TS14,TS15,TS16]

TS01 = (array01[0],array02[0],array03[0],array04[0],array05[0],array06[0],array07[0],array08[0],array09[0],array10[0],array11[0],array12[0],array13[0],array14[0],array15[0],array16[0],array17[0],array18[0],array19[0],array20[0])
TS02 = (array01[1],array02[1],array03[1],array04[1],array05[1],array06[1],array07[1],array08[1],array09[1],array10[1],array11[1],array12[1],array13[1],array14[1],array15[1],array16[1],array17[1],array18[1],array19[1],array20[1])
TS03 = (array01[2],array02[2],array03[2],array04[2],array05[2],array06[2],array07[2],array08[2],array09[2],array10[2],array11[2],array12[2],array13[2],array14[2],array15[2],array16[2],array17[2],array18[2],array19[2],array20[2])
TS04 = (array01[3],array02[3],array03[3],array04[3],array05[3],array06[3],array07[3],array08[3],array09[3],array10[3],array11[3],array12[3],array13[3],array14[3],array15[3],array16[3],array17[3],array18[3],array19[3],array20[3])
TS05 = (array01[4],array02[4],array03[4],array04[4],array05[4],array06[4],array07[4],array08[4],array09[4],array10[4],array11[4],array12[4],array13[4],array14[4],array15[4],array16[4],array17[4],array18[4],array19[4],array20[4])
TS06 = (array01[5],array02[5],array03[5],array04[5],array05[5],array06[5],array07[5],array08[5],array09[5],array10[5],array11[5],array12[5],array13[5],array14[5],array15[5],array16[5],array17[5],array18[5],array19[5],array20[5])
TS07 = (array01[6],array02[6],array03[6],array04[6],array05[6],array06[6],array07[6],array08[6],array09[6],array10[6],array11[6],array12[6],array13[6],array14[6],array15[6],array16[6],array17[6],array18[6],array19[6],array20[6])
TS08 = (array01[7],array02[7],array03[7],array04[7],array05[7],array06[7],array07[7],array08[7],array09[7],array10[7],array11[7],array12[7],array13[7],array14[7],array15[7],array16[7],array17[7],array18[7],array19[7],array20[7])
TS09 = (array01[8],array02[8],array03[8],array04[8],array05[8],array06[8],array07[8],array08[8],array09[8],array10[8],array11[8],array12[8],array13[8],array14[8],array15[8],array16[8],array17[8],array18[8],array19[8],array20[8])
TS10 = (array01[9],array02[9],array03[9],array04[9],array05[9],array06[9],array07[9],array08[9],array09[9],array10[9],array11[9],array12[9],array13[9],array14[9],array15[9],array16[9],array17[9],array18[9],array19[9],array20[9])
TS11 = (array01[10],array02[10],array03[10],array04[10],array05[10],array06[10],array07[10],array08[10],array09[10],array10[10],array11[10],array12[10],array13[10],array14[10],array15[10],array16[10],array17[10],array18[10],array19[10],array20[10])
TS12 = (array01[11],array02[11],array03[11],array04[11],array05[11],array06[11],array07[11],array08[11],array09[11],array10[11],array11[11],array12[11],array13[11],array14[11],array15[11],array16[11],array17[11],array18[11],array19[11],array20[11])
TS13 = (array01[12],array02[12],array03[12],array04[12],array05[12],array06[12],array07[12],array08[12],array09[12],array10[12],array11[12],array12[12],array13[12],array14[12],array15[12],array16[12],array17[12],array18[12],array19[12],array20[12])
TS14 = (array01[13],array02[13],array03[13],array04[13],array05[13],array06[13],array07[13],array08[13],array09[13],array10[13],array11[13],array12[13],array13[13],array14[13],array15[13],array16[13],array17[13],array18[13],array19[13],array20[13])
TS15 = (array01[14],array02[14],array03[14],array04[14],array05[14],array06[14],array07[14],array08[14],array09[14],array10[14],array11[14],array12[14],array13[14],array14[14],array15[14],array16[14],array17[14],array18[14],array19[14],array20[14])
TS16 = (array01[15],array02[15],array03[15],array04[15],array05[15],array06[15],array07[15],array08[15],array09[15],array10[15],array11[15],array12[15],array13[15],array14[15],array15[15],array16[15],array17[15],array18[15],array19[15],array20[15])


##     OVERCURTAILMENT     ##
#penalty for curtailing more than necessary
OCtotalpenalty = 0
OCpenaltyvalue = 10000

if (array01.size - np.count_nonzero(Farray01)) > maxoff01:
    OCtotalpenalty += 1
    
if (array02.size - np.count_nonzero(Farray02)) > maxoff02:
    OCtotalpenalty += 1
    
if (array03.size - np.count_nonzero(Farray03)) > maxoff03:
    OCtotalpenalty += 1
    
if (array04.size - np.count_nonzero(Farray04)) > maxoff04:
    OCtotalpenalty += 1
    
if (array05.size - np.count_nonzero(Farray05)) > maxoff05:
    OCtotalpenalty += 1

if (array06.size - np.count_nonzero(Farray06)) > maxoff06:
    OCtotalpenalty += 1

if (array07.size - np.count_nonzero(Farray07)) > maxoff07:
    OCtotalpenalty += 1

if (array08.size - np.count_nonzero(Farray08)) > maxoff08:
    OCtotalpenalty += 1

if (array09.size - np.count_nonzero(Farray09)) > maxoff09:
    OCtotalpenalty += 1

if (array10.size - np.count_nonzero(Farray10)) > maxoff10:
    OCtotalpenalty += 1

if (array11.size - np.count_nonzero(Farray11)) > maxoff11:
    OCtotalpenalty += 1

if (array12.size - np.count_nonzero(Farray12)) > maxoff12:
    OCtotalpenalty += 1

if (array13.size - np.count_nonzero(Farray13)) > maxoff13:
    OCtotalpenalty += 1

if (array14.size - np.count_nonzero(Farray14)) > maxoff14:
    OCtotalpenalty += 1

if (array15.size - np.count_nonzero(Farray15)) > maxoff15:
    OCtotalpenalty += 1

if (array16.size - np.count_nonzero(Farray16)) > maxoff16:
    OCtotalpenalty += 1

if (array17.size - np.count_nonzero(Farray17)) > maxoff17:
    OCtotalpenalty += 1

if (array18.size - np.count_nonzero(Farray18)) > maxoff18:
    OCtotalpenalty += 1

if (array19.size - np.count_nonzero(Farray19)) > maxoff19:
    OCtotalpenalty += 1

if (array20.size - np.count_nonzero(Farray20)) > maxoff20:
    OCtotalpenalty += 1

OCFinalTotalPenalty = OCtotalpenalty*OCpenaltyvalue

print('Total Penalty from Over Curtailment', OCFinalTotalPenalty)


##     UNDERCURTAILMENT     ##
#penalty for undercurtailing
UCtotalpenalty = 0
UCpenaltyvalue = 10000

if np.count_nonzero(Farray01) < minon01:
    UCtotalpenalty += 1
    
if np.count_nonzero(Farray02) < minon02:
    UCtotalpenalty += 1
    
if np.count_nonzero(Farray03) < minon03:
    UCtotalpenalty += 1
    
if np.count_nonzero(Farray04) < minon04:
    UCtotalpenalty += 1
    
if np.count_nonzero(Farray05) < minon05:
    UCtotalpenalty += 1

if np.count_nonzero(Farray06) < minon06:
    UCtotalpenalty += 1

if np.count_nonzero(Farray07) < minon07:
    UCtotalpenalty += 1

if np.count_nonzero(Farray08) < minon08:
    UCtotalpenalty += 1

if np.count_nonzero(Farray09) < minon09:
    UCtotalpenalty += 1

if np.count_nonzero(Farray10) < minon10:
    UCtotalpenalty += 1

if np.count_nonzero(Farray11) < minon11:
    UCtotalpenalty += 1

if np.count_nonzero(Farray12) < minon12:
    UCtotalpenalty += 1

if np.count_nonzero(Farray13) < minon13:
    UCtotalpenalty += 1

if np.count_nonzero(Farray14) < minon14:
    UCtotalpenalty += 1

if np.count_nonzero(Farray15) < minon15:
    UCtotalpenalty += 1

if np.count_nonzero(Farray16) < minon16:
    UCtotalpenalty += 1

if np.count_nonzero(Farray17) < minon17:
    UCtotalpenalty += 1

if np.count_nonzero(Farray18) < minon18:
    UCtotalpenalty += 1

if np.count_nonzero(Farray19) < minon19:
    UCtotalpenalty += 1

if np.count_nonzero(Farray20) < minon20:
    UCtotalpenalty += 1

UCFinalTotalPenalty = UCtotalpenalty*UCpenaltyvalue
print('Total Penalty from Under Curtailment', UCFinalTotalPenalty)


##     REQUIRED CURTAILMENT     ##
#penalty for not meeting required curtailment per timeslot
RCtotalpenalty = 0
RCpenaltyvalue = 100000

if np.sum(np.multiply(TS01,Fconsumption)) < TSlimit01:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS02,Fconsumption)) < TSlimit02:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS03,Fconsumption)) < TSlimit03:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS04,Fconsumption)) < TSlimit04:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS05,Fconsumption)) < TSlimit05:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS06,Fconsumption)) < TSlimit06:
    RCtotalpenalty += 1
    
if np.sum(np.multiply(TS07,Fconsumption)) < TSlimit07:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS08,Fconsumption)) < TSlimit08:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS09,Fconsumption)) < TSlimit09:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS10,Fconsumption)) < TSlimit10:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS11,Fconsumption)) < TSlimit11:
    RCtotalpenalty += 1
    
if np.sum(np.multiply(TS12,Fconsumption)) < TSlimit12:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS13,Fconsumption)) < TSlimit13:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS14,Fconsumption)) < TSlimit14:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS15,Fconsumption)) < TSlimit15:
    RCtotalpenalty += 1

if np.sum(np.multiply(TS16,Fconsumption)) < TSlimit16:
    RCtotalpenalty += 1    

RCFinalTotalPenalty = RCtotalpenalty*RCpenaltyvalue
print('Total Penalty from Required Curtailment', RCFinalTotalPenalty)


##     EXCESS CURTAILMENT     ##
Epenaltyvalue = 1000

E01 = np.sum(np.multiply(TS01,Fconsumption)) - TSlimit01
E02 = np.sum(np.multiply(TS02,Fconsumption)) - TSlimit02
E03 = np.sum(np.multiply(TS03,Fconsumption)) - TSlimit03
E04 = np.sum(np.multiply(TS04,Fconsumption)) - TSlimit04
E05 = np.sum(np.multiply(TS05,Fconsumption)) - TSlimit05
E06 = np.sum(np.multiply(TS06,Fconsumption)) - TSlimit06
E07 = np.sum(np.multiply(TS07,Fconsumption)) - TSlimit07
E08 = np.sum(np.multiply(TS08,Fconsumption)) - TSlimit08
E09 = np.sum(np.multiply(TS09,Fconsumption)) - TSlimit09
E10 = np.sum(np.multiply(TS10,Fconsumption)) - TSlimit10
E11 = np.sum(np.multiply(TS11,Fconsumption)) - TSlimit11
E12 = np.sum(np.multiply(TS12,Fconsumption)) - TSlimit12
E13 = np.sum(np.multiply(TS13,Fconsumption)) - TSlimit13
E14 = np.sum(np.multiply(TS14,Fconsumption)) - TSlimit14
E15 = np.sum(np.multiply(TS15,Fconsumption)) - TSlimit15
E16 = np.sum(np.multiply(TS16,Fconsumption)) - TSlimit16

AE01 = abs(E01)
AE02 = abs(E02)
AE03 = abs(E03)
AE04 = abs(E04)
AE05 = abs(E05)
AE06 = abs(E06)
AE07 = abs(E07)
AE08 = abs(E08)
AE09 = abs(E09)
AE10 = abs(E10)
AE11 = abs(E11)
AE12 = abs(E12)
AE13 = abs(E13)
AE14 = abs(E14)
AE15 = abs(E15)
AE16 = abs(E16)

excessarray = (E01,E02,E03,E04,E05,E06,E07,E08,E09,E10,E11,E12,E13,E14,E15,E16)
totalexcess = AE01+AE02+AE03+AE04+AE05+AE06+AE07+AE08+AE09+AE10+AE11+AE12+AE13+AE14+AE15+AE16
PenaltyExcess = totalexcess*Epenaltyvalue
print('Total Penalty from Excess Curtailment', PenaltyExcess)


##     CONTINUITY     ##
#to make sure the curtailments are in continuous chunks, ideally one long curtailment
Cpenalty = 0
Cpenaltyvalue = 10000

if np.count_nonzero(np.diff(Farray01)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray02)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray03)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray04)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray05)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray06)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray07)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray08)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray09)==-1) > 1:
    Cpenalty += 1
    
if np.count_nonzero(np.diff(Farray10)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray11)==-1) > 1:
    Cpenalty += 1
    
if np.count_nonzero(np.diff(Farray12)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray13)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray14)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray15)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray16)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray17)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray18)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray19)==-1) > 1:
    Cpenalty += 1

if np.count_nonzero(np.diff(Farray20)==-1) > 1:
    Cpenalty += 1
 
Ctotalpenalty = Cpenalty*Cpenaltyvalue
print('Total Penalty from Continuity', Ctotalpenalty)


#####double check first before submission
OF = DUTotal + SelfLoadTotal + OCFinalTotalPenalty + UCFinalTotalPenalty + RCFinalTotalPenalty + PenaltyExcess + Ctotalpenalty
print('OF', OF)
print('Array of overcurtailment in kW: \n', excessarray)








    
