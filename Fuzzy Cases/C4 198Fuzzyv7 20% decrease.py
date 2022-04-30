import numpy as np
import skfuzzy as fuzz

#hardcode per array and consumption load given that scikit fuzzy functions are mostly math functions
# Progress:
# DUCost: OK
# SelfCost: OK
# Overcurtailment: OK
# Undercurtailment: OK
# RequiredCurtailment : OK
# ExcessCurtailment : OK

#set costs per kW here
DUcost = 10
SGEcost = 5
#capacity consumption; consX -> arrayX
Ctotal = []
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

#####   SELF GENERATED LOAD     #####

def SGEgenerate(mode):
    #amount of self generated energy per load
    self01 = 15
    self02 = 7
    self03 = 2
    self04 = 5
    self05 = 8
    self06 = 9
    self07 = 6
    self08 = 3
    self09 = 17
    self10 = 3
    self11 = 2
    self12 = 1
    self13 = 6
    self14 = 4
    self15 = 2
    self16 = 13
    self17 = 12
    self18 = 9
    self19 = 2
    self20 = 3

    #SGE is off
    if mode == 0:
        SGE = np.zeros(320)
        
    #SGE is constant
    if mode == 1:
        SGE = []
        T01 = np.full(16,self01)
        T02 = np.full(16,self02)
        T03 = np.full(16,self03)
        T04 = np.full(16,self04)
        T05 = np.full(16,self05)
        T06 = np.full(16,self06)
        T07 = np.full(16,self07)
        T08 = np.full(16,self08)
        T09 = np.full(16,self09)
        T10 = np.full(16,self10)
        T11 = np.full(16,self11)
        T12 = np.full(16,self12)
        T13 = np.full(16,self13)
        T14 = np.full(16,self14)
        T15 = np.full(16,self15)
        T16 = np.full(16,self16)
        T17 = np.full(16,self17)
        T18 = np.full(16,self18)
        T19 = np.full(16,self19)
        T20 = np.full(16,self20)
        
        SGE = np.append(SGE,[T01,T02,T03,T04,T05,T06,T07,T08,T09,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20])
    
    #SGE is random value but on
    if mode == 2:
        SGE = []
        T01 = np.random.randint(self01+1,size=16)
        T02 = np.random.randint(self02+1,size=16)
        T03 = np.random.randint(self03+1,size=16)
        T04 = np.random.randint(self04+1,size=16)
        T05 = np.random.randint(self05+1,size=16)
        T06 = np.random.randint(self06+1,size=16)
        T07 = np.random.randint(self07+1,size=16)
        T08 = np.random.randint(self08+1,size=16)
        T09 = np.random.randint(self09+1,size=16)
        T10 = np.random.randint(self10+1,size=16)
        T11 = np.random.randint(self11+1,size=16)
        T12 = np.random.randint(self12+1,size=16)
        T13 = np.random.randint(self13+1,size=16)
        T14 = np.random.randint(self14+1,size=16)
        T15 = np.random.randint(self15+1,size=16)
        T16 = np.random.randint(self16+1,size=16)
        T17 = np.random.randint(self17+1,size=16)
        T18 = np.random.randint(self18+1,size=16)
        T19 = np.random.randint(self19+1,size=16)
        T20 = np.random.randint(self20+1,size=16)

        
        SGE = np.append(SGE,[T01,T02,T03,T04,T05,T06,T07,T08,T09,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20])

    
    #SGE is fixed value but on or off randomly
    if mode == 3:
        SGE = []
        T01 = np.full(16,self01)
        T02 = np.full(16,self02)
        T03 = np.full(16,self03)
        T04 = np.full(16,self04)
        T05 = np.full(16,self05)
        T06 = np.full(16,self06)
        T07 = np.full(16,self07)
        T08 = np.full(16,self08)
        T09 = np.full(16,self09)
        T10 = np.full(16,self10)
        T11 = np.full(16,self11)
        T12 = np.full(16,self12)
        T13 = np.full(16,self13)
        T14 = np.full(16,self14)
        T15 = np.full(16,self15)
        T16 = np.full(16,self16)
        T17 = np.full(16,self17)
        T18 = np.full(16,self18)
        T19 = np.full(16,self19)
        T20 = np.full(16,self20)
        
        SGE = np.append(SGE,[T01,T02,T03,T04,T05,T06,T07,T08,T09,T10,T11,T12,T13,T14,T15,T16,T17,T18,T19,T20])
        rand = np.random.randint(2,size=320)
        SGE = np.multiply(SGE,rand)
        
    return SGE

#####    DU SUPPLIED COST AND SELF SUPPLIED COST     #####

SGE = SGEgenerate(1)
#call defined SGEgenerate function and setup

SGE01 = SGE[0:16]
SGE02 = SGE[16:16*2]
SGE03 = SGE[16*2:16*3]
SGE04 = SGE[16*3:16*4]
SGE05 = SGE[16*4:16*5]
SGE06 = SGE[16*5:16*6]
SGE07 = SGE[16*6:16*7]
SGE08 = SGE[16*7:16*8]
SGE09 = SGE[16*8:16*9]
SGE10 = SGE[16*9:16*10]
SGE11 = SGE[16*10:16*11]
SGE12 = SGE[16*11:16*12]
SGE13 = SGE[16*12:16*13]
SGE14 = SGE[16*13:16*14]
SGE15 = SGE[16*14:16*15]
SGE16 = SGE[16*15:16*16]
SGE17 = SGE[16*16:16*17]
SGE18 = SGE[16*17:16*18]
SGE19 = SGE[16*18:16*19]
SGE20 = SGE[16*19:16*20]
##uncomment the line below for debugging of SGEXX
#print('SGE01', SGE01)

#get solo value for calculation purposes
S01 = np.nanmax(SGE01)
S02 = np.nanmax(SGE02)
S03 = np.nanmax(SGE03)
S04 = np.nanmax(SGE04)
S05 = np.nanmax(SGE05)
S06 = np.nanmax(SGE06)
S07 = np.nanmax(SGE07)
S08 = np.nanmax(SGE08)
S09 = np.nanmax(SGE09)
S10 = np.nanmax(SGE10)
S11 = np.nanmax(SGE11)
S12 = np.nanmax(SGE12)
S13 = np.nanmax(SGE13)
S14 = np.nanmax(SGE14)
S15 = np.nanmax(SGE15)
S16 = np.nanmax(SGE16)
S17 = np.nanmax(SGE17)
S18 = np.nanmax(SGE18)
S19 = np.nanmax(SGE19)
S20 = np.nanmax(SGE20)
##uncomment the line below for debugging of SXX
#print('S01', S01)


#fuzz.sigmoid applied on the arrays to apply Fuzzy logic
#skfuzzy.sigmoid(x, power, split=0.5)
#x : ndarray; Input vector or image array. Should be pre-normalized to range [0, 1]
#p : float; Power of the intensification (p > 0). Experiment with small, decimal values and increase as necessary.
## changing the value of p affects the values of array in performing fuzz.sigmoid, a form of sensitivity analysis
#split : floatThreshold for intensification. Values above split will be intensified,
#while values below split will be deintensified. Note range for split is (0, 1). Default of 0.5 is reasonable for many well-exposed images
##split value set to default 0.5

#fuzz.sigmf(x, b, c)

Xarray01 = fuzz.sigmoid(array01, 2, split=0.5)
Xarray02 = fuzz.sigmoid(array02, 2, split=0.5)
Xarray03 = fuzz.sigmoid(array03, 2, split=0.5)
Xarray04 = fuzz.sigmoid(array04, 2, split=0.5)
Xarray05 = fuzz.sigmoid(array05, 2, split=0.5)
Xarray06 = fuzz.sigmoid(array06, 2, split=0.5)
Xarray07 = fuzz.sigmoid(array07, 2, split=0.5)
Xarray08 = fuzz.sigmoid(array08, 2, split=0.5)
Xarray09 = fuzz.sigmoid(array09, 2, split=0.5)
Xarray10 = fuzz.sigmoid(array10, 2, split=0.5)
Xarray11 = fuzz.sigmoid(array11, 2, split=0.5)
Xarray12 = fuzz.sigmoid(array12, 2, split=0.5)
Xarray13 = fuzz.sigmoid(array13, 2, split=0.5)
Xarray14 = fuzz.sigmoid(array14, 2, split=0.5)
Xarray15 = fuzz.sigmoid(array15, 2, split=0.5)
Xarray16 = fuzz.sigmoid(array16, 2, split=0.5)
Xarray17 = fuzz.sigmoid(array17, 2, split=0.5)
Xarray18 = fuzz.sigmoid(array18, 2, split=0.5)
Xarray19 = fuzz.sigmoid(array19, 2, split=0.5)
Xarray20 = fuzz.sigmoid(array20, 2, split=0.5)
# 0's become 0.26894; 1's become 0.73106
#print('Farray01',Farray01) #use this line and sub the numbers for debugging
#Calculate DU Load
#muliply capacity consumption value by the fuzzified array

CS01 = C01-S01
CS02 = C02-S02
CS03 = C03-S03
CS04 = C04-S04
CS05 = C05-S05
CS06 = C06-S06
CS07 = C07-S07
CS08 = C08-S08
CS09 = C09-S09
CS10 = C10-S10
CS11 = C11-S11
CS12 = C12-S12
CS13 = C13-S13
CS14 = C14-S14
CS15 = C15-S15
CS16 = C16-S16
CS17 = C17-S17
CS18 = C18-S18
CS19 = C19-S19
CS20 = C20-S20

DU01 = np.multiply(CS01, Xarray01)
DU02 = np.multiply(CS02, Xarray02)
DU03 = np.multiply(CS03, Xarray03)
DU04 = np.multiply(CS04, Xarray04)
DU05 = np.multiply(CS05, Xarray05)
DU06 = np.multiply(CS06, Xarray06)
DU07 = np.multiply(CS07, Xarray07)
DU08 = np.multiply(CS08, Xarray08)
DU09 = np.multiply(CS09, Xarray09)
DU10 = np.multiply(CS10, Xarray10)
DU11 = np.multiply(CS11, Xarray11)
DU12 = np.multiply(CS12, Xarray12)
DU13 = np.multiply(CS13, Xarray13)
DU14 = np.multiply(CS14, Xarray14)
DU15 = np.multiply(CS15, Xarray15)
DU16 = np.multiply(CS16, Xarray16)
DU17 = np.multiply(CS17, Xarray17)
DU18 = np.multiply(CS18, Xarray18)
DU19 = np.multiply(CS19, Xarray19)
DU20 = np.multiply(CS20, Xarray20)

#total req - consumed energy is already done here
DFU01 = np.nanmax(DU01) #gets the value that(correlates to 1) multiplied by the DU Load
DFU02 = np.nanmax(DU02)
DFU03 = np.nanmax(DU03)
DFU04 = np.nanmax(DU04)
DFU05 = np.nanmax(DU05)
DFU06 = np.nanmax(DU06)
DFU07 = np.nanmax(DU07)
DFU08 = np.nanmax(DU08)
DFU09 = np.nanmax(DU09)
DFU10 = np.nanmax(DU10)
DFU11 = np.nanmax(DU11)
DFU12 = np.nanmax(DU12)
DFU13 = np.nanmax(DU13)
DFU14 = np.nanmax(DU14)
DFU15 = np.nanmax(DU15)
DFU16 = np.nanmax(DU16)
DFU17 = np.nanmax(DU17)
DFU18 = np.nanmax(DU18)
DFU19 = np.nanmax(DU19)
DFU20 = np.nanmax(DU20)

#use print('DFUXX: ', DFUXX)  and uncomment for debugging
#print('DFU01: ', DFU01) 
#print('DFU02: ', DFU02)
#print('DFU03: ', DFU03)
#print('DFU04: ', DFU04)
#print('DFU05: ', DFU05)
#print('DFU06: ', DFU06)
#print('DFU07: ', DFU07)
#print('DFU08: ', DFU08)
#print('DFU09: ', DFU09)
#print('DFU10: ', DFU10)
#print('DFU11: ', DFU11)
#print('DFU12: ', DFU12)
#print('DFU13: ', DFU13)
#print('DFU14: ', DFU14)
#print('DFU15: ', DFU15)
#print('DFU16: ', DFU16)
#print('DFU17: ', DFU17)
#print('DFU18: ', DFU18)
#print('DFU19: ', DFU19)
#print('DFU20: ', DFU20)

FXarray01 = np.multiply(Xarray01, array01)
FXarray02 = np.multiply(Xarray02, array02)
FXarray03 = np.multiply(Xarray03, array03)
FXarray04 = np.multiply(Xarray04, array04)
FXarray05 = np.multiply(Xarray05, array05)
FXarray06 = np.multiply(Xarray06, array06)
FXarray07 = np.multiply(Xarray07, array07)
FXarray08 = np.multiply(Xarray08, array08)
FXarray09 = np.multiply(Xarray09, array09)
FXarray10 = np.multiply(Xarray10, array10)
FXarray11 = np.multiply(Xarray11, array11)
FXarray12 = np.multiply(Xarray12, array12)
FXarray13 = np.multiply(Xarray13, array13)
FXarray14 = np.multiply(Xarray14, array14)
FXarray15 = np.multiply(Xarray15, array15)
FXarray16 = np.multiply(Xarray16, array16)
FXarray17 = np.multiply(Xarray17, array17)
FXarray18 = np.multiply(Xarray18, array18)
FXarray19 = np.multiply(Xarray19, array19)
FXarray20 = np.multiply(Xarray20, array20)

Farray01 = np.multiply(DFU01, array01)
Farray02 = np.multiply(DFU02, array02)
Farray03 = np.multiply(DFU03, array03)
Farray04 = np.multiply(DFU04, array04)
Farray05 = np.multiply(DFU05, array05)
Farray06 = np.multiply(DFU06, array06)
Farray07 = np.multiply(DFU07, array07)
Farray08 = np.multiply(DFU08, array08)
Farray09 = np.multiply(DFU09, array09)
Farray10 = np.multiply(DFU10, array10)
Farray11 = np.multiply(DFU11, array11)
Farray12 = np.multiply(DFU12, array12)
Farray13 = np.multiply(DFU13, array13)
Farray14 = np.multiply(DFU14, array14)
Farray15 = np.multiply(DFU15, array15)
Farray16 = np.multiply(DFU16, array16)
Farray17 = np.multiply(DFU17, array17)
Farray18 = np.multiply(DFU18, array18)
Farray19 = np.multiply(DFU19, array19)
Farray20 = np.multiply(DFU20, array20)



#use print('FarrayXX \n', FarrayXX) and uncomment for debugging; shows new array
#print('Farray01 \n', Farray01)
#print('FXarray01 \n', FXarray01)



DUTotal = DFU01+DFU02+DFU03+DFU04+DFU05+DFU06+DFU07+DFU08+DFU09+DFU10+DFU11+DFU12+DFU13+DFU14+DFU15+DFU16+DFU17+DFU18+DFU19+DFU20

#print('DU Max Total', DUTotal)

#####   CURTAILMENT COST AND OVERCURTAILMENT     #####

#arbitrary penalty values
penaltyvalue = 1

#limit for each TS
TSlimit01 = 110*0.8
TSlimit02 = 230*0.8
TSlimit03 = 455*0.8
TSlimit04 = 680*0.8
TSlimit05 = 770*0.8
TSlimit06 = 800*0.8
TSlimit07 = 750*0.8
TSlimit08 = 640*0.8
TSlimit09 = 590*0.8
TSlimit10 = 610*0.8
TSlimit11 = 660*0.8
TSlimit12 = 680*0.8
TSlimit13 = 570*0.8
TSlimit14 = 410*0.8
TSlimit15 = 230*0.8
TSlimit16 = 135*0.8

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

consumption = [CS01,CS02,CS03,CS04,CS05,CS06,CS07,CS08,CS09,CS10,CS11,CS12,CS13,CS14,CS15,CS16,CS17,CS18,CS19,CS20]

#Fconsumption shows the array of fuzzifed consumption values
Fconsumption = [DFU01,DFU02,DFU03,DFU04,DFU05,DFU06,DFU07,DFU08,DFU09,DFU10,DFU11,DFU12,DFU13,DFU14,DFU15,DFU16,DFU17,DFU18,DFU19,DFU20]
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

#TSarray = (TS01, TS02, TS03, TS04, TS05, TS06, TS07, TS08, TS09, TS10, TS11, TS12, TS13, TS14, TS15, TS16)
#print('TSarray', TSarray)
#print('np.sum TS01',np.sum(TS01))

##     OVERCURTAILMENT     ##
#penalty for curtailing more than necessary
OCtotalpenalty = 0
OCpenaltyvalue = 10000

if (array01.size - np.sum(Xarray01)) > maxoff01:
    OCtotalpenalty += 1
    
if (array02.size - np.sum(Xarray02)) > maxoff02:
    OCtotalpenalty += 1
    
if (array03.size - np.sum(Xarray03)) > maxoff03:
    OCtotalpenalty += 1
    
if (array04.size - np.sum(Xarray04)) > maxoff04:
    OCtotalpenalty += 1
    
if (array05.size - np.sum(Xarray05)) > maxoff05:
    OCtotalpenalty += 1

if (array06.size - np.sum(Xarray06)) > maxoff06:
    OCtotalpenalty += 1

if (array07.size - np.sum(Xarray07)) > maxoff07:
    OCtotalpenalty += 1

if (array08.size - np.sum(Xarray08)) > maxoff08:
    OCtotalpenalty += 1

if (array09.size - np.sum(Xarray09)) > maxoff09:
    OCtotalpenalty += 1

if (array10.size - np.sum(Xarray10)) > maxoff10:
    OCtotalpenalty += 1

if (array11.size - np.sum(Xarray11)) > maxoff11:
    OCtotalpenalty += 1

if (array12.size - np.sum(Xarray12)) > maxoff12:
    OCtotalpenalty += 1

if (array13.size - np.sum(Xarray13)) > maxoff13:
    OCtotalpenalty += 1

if (array14.size - np.sum(Xarray14)) > maxoff14:
    OCtotalpenalty += 1

if (array15.size - np.sum(Xarray15)) > maxoff15:
    OCtotalpenalty += 1

if (array16.size - np.sum(Xarray16)) > maxoff16:
    OCtotalpenalty += 1

if (array17.size - np.sum(Xarray17)) > maxoff17:
    OCtotalpenalty += 1

if (array18.size - np.sum(Xarray18)) > maxoff18:
    OCtotalpenalty += 1

if (array19.size - np.sum(Xarray19)) > maxoff19:
    OCtotalpenalty += 1

if (array20.size - np.sum(Xarray20)) > maxoff20:
    OCtotalpenalty += 1

OCFinalTotalPenalty = OCtotalpenalty*OCpenaltyvalue
#print('Total Penalty from Over Curtailment', OCFinalTotalPenalty)


##     UNDERCURTAILMENT     ##
#penalty for undercurtailing
UCtotalpenalty = 0
UCpenaltyvalue = 10000

if np.count_nonzero(Xarray01) < minon01:
    UCtotalpenalty += 1
    
if np.count_nonzero(Xarray02) < minon02:
    UCtotalpenalty += 1
    
if np.count_nonzero(Xarray03) < minon03:
    UCtotalpenalty += 1
    
if np.count_nonzero(Xarray04) < minon04:
    UCtotalpenalty += 1
    
if np.count_nonzero(Xarray05) < minon05:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray06) < minon06:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray07) < minon07:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray08) < minon08:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray09) < minon09:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray10) < minon10:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray11) < minon11:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray12) < minon12:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray13) < minon13:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray14) < minon14:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray15) < minon15:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray16) < minon16:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray17) < minon17:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray18) < minon18:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray19) < minon19:
    UCtotalpenalty += 1

if np.count_nonzero(Xarray20) < minon20:
    UCtotalpenalty += 1

UCFinalTotalPenalty = UCtotalpenalty*UCpenaltyvalue
#print('Total Penalty from Under Curtailment', UCFinalTotalPenalty)


##     REQUIRED CURTAILMENT     ##
#penalty for not meeting required curtailment per timeslot
RCtotalpenalty = 0
RCpenaltyvalue = 100000

inv = np.ones(20,dtype=int)

if np.sum(np.multiply((np.subtract(inv,TS01)),Fconsumption)) < TSlimit01:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS02)),Fconsumption)) < TSlimit02:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS03)),Fconsumption)) < TSlimit03:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS04)),Fconsumption)) < TSlimit04:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS05)),Fconsumption)) < TSlimit05:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS06)),Fconsumption)) < TSlimit06:
    RCtotalpenalty += 1
    
if np.sum(np.multiply((np.subtract(inv,TS07)),Fconsumption)) < TSlimit07:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS08)),Fconsumption)) < TSlimit08:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS09)),Fconsumption)) < TSlimit09:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS10)),Fconsumption)) < TSlimit10:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS11)),Fconsumption)) < TSlimit11:
    RCtotalpenalty += 1
    
if np.sum(np.multiply((np.subtract(inv,TS12)),Fconsumption)) < TSlimit12:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS13)),Fconsumption)) < TSlimit13:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS14)),Fconsumption)) < TSlimit14:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS15)),Fconsumption)) < TSlimit15:
    RCtotalpenalty += 1

if np.sum(np.multiply((np.subtract(inv,TS16)),Fconsumption)) < TSlimit16:
    RCtotalpenalty += 1    

RCFinalTotalPenalty = RCtotalpenalty*RCpenaltyvalue
#print('Total Penalty from Required Curtailment', RCFinalTotalPenalty)


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
#print('Total Penalty from Excess Curtailment', PenaltyExcess)

#print('excessarray', excessarray)

OF = np.sum(np.multiply(Farray01,DUcost))+np.sum(np.multiply((np.multiply(S01,SGEcost)),FXarray01)) + np.sum(np.multiply(Farray02,DUcost))+np.sum(np.multiply((np.multiply(S02,SGEcost)),FXarray02)) +\
     np.sum(np.multiply(Farray03,DUcost))+np.sum(np.multiply((np.multiply(S03,SGEcost)),FXarray03)) + np.sum(np.multiply(Farray04,DUcost))+np.sum(np.multiply((np.multiply(S04,SGEcost)),FXarray04)) +\
     np.sum(np.multiply(Farray05,DUcost))+np.sum(np.multiply((np.multiply(S05,SGEcost)),FXarray05)) + np.sum(np.multiply(Farray06,DUcost))+np.sum(np.multiply((np.multiply(S06,SGEcost)),FXarray06)) +\
     np.sum(np.multiply(Farray07,DUcost))+np.sum(np.multiply((np.multiply(S07,SGEcost)),FXarray07)) + np.sum(np.multiply(Farray08,DUcost))+np.sum(np.multiply((np.multiply(S08,SGEcost)),FXarray08)) +\
     np.sum(np.multiply(Farray09,DUcost))+np.sum(np.multiply((np.multiply(S09,SGEcost)),FXarray09)) + np.sum(np.multiply(Farray10,DUcost))+np.sum(np.multiply((np.multiply(S10,SGEcost)),FXarray10)) +\
     np.sum(np.multiply(Farray11,DUcost))+np.sum(np.multiply((np.multiply(S11,SGEcost)),FXarray11)) + np.sum(np.multiply(Farray12,DUcost))+np.sum(np.multiply((np.multiply(S12,SGEcost)),FXarray12)) +\
     np.sum(np.multiply(Farray13,DUcost))+np.sum(np.multiply((np.multiply(S13,SGEcost)),FXarray13)) + np.sum(np.multiply(Farray14,DUcost))+np.sum(np.multiply((np.multiply(S14,SGEcost)),FXarray14)) +\
     np.sum(np.multiply(Farray15,DUcost))+np.sum(np.multiply((np.multiply(S15,SGEcost)),FXarray15)) + np.sum(np.multiply(Farray16,DUcost))+np.sum(np.multiply((np.multiply(S16,SGEcost)),FXarray16)) +\
     np.sum(np.multiply(Farray17,DUcost))+np.sum(np.multiply((np.multiply(S17,SGEcost)),FXarray17)) + np.sum(np.multiply(Farray18,DUcost))+np.sum(np.multiply((np.multiply(S18,SGEcost)),FXarray18)) +\
     np.sum(np.multiply(Farray19,DUcost))+np.sum(np.multiply((np.multiply(S19,SGEcost)),FXarray19)) + np.sum(np.multiply(Farray20,DUcost))+np.sum(np.multiply((np.multiply(S20,SGEcost)),FXarray20)) +\
     OCFinalTotalPenalty + UCFinalTotalPenalty + RCFinalTotalPenalty + PenaltyExcess 
#print('DUTotal', DUTotal)
print('OF', OF)


print('Schedule of Load 01:', array01)
print("L01 min on time:", minon01)
print("L01 on time:", np.count_nonzero(array01))
print("L01 max off time:", maxoff01)
print("L01 off time:", 16-np.count_nonzero(array01))

print('Schedule of Load 02:', array02)
print("L02 min on time:", minon02)
print("L02 on time:", np.count_nonzero(array02))
print("L02 max off time:", maxoff02)
print("L02 off time:", 16-np.count_nonzero(array02))

print('Schedule of Load 03:', array03)
print("L03 min on time:", minon03)
print("L03 on time:", np.count_nonzero(array03))
print("L03 max off time:", maxoff03)
print("L03 off time:", 16-np.count_nonzero(array03))

print('Schedule of Load 04:', array04)
print("L04 min on time:", minon04)
print("L04 on time:", np.count_nonzero(array04))
print("L04 max off time:", maxoff04)
print("L04 off time:", 16-np.count_nonzero(array04))

print('Schedule of Load 05:', array05)
print("L05 min on time:", minon05)
print("L05 on time:", np.count_nonzero(array05))
print("L05 max off time:", maxoff05)
print("L05 off time:", 16-np.count_nonzero(array05))

print('Schedule of Load 06:', array06)
print("L06 min on time:", minon06)
print("L06 on time:", np.count_nonzero(array06))
print("L06 max off time:", maxoff06)
print("L06 off time:", 16-np.count_nonzero(array06))

print('Schedule of Load 07:', array07)
print("L07 min on time:", minon07)
print("L07 on time:", np.count_nonzero(array07))
print("L07 max off time:", maxoff07)
print("L07 off time:", 16-np.count_nonzero(array07))

print('Schedule of Load 08:', array08)
print("L08 min on time:", minon08)
print("L08 on time:", np.count_nonzero(array08))
print("L08 max off time:", maxoff08)
print("L08 off time:", 16-np.count_nonzero(array08))

print('Schedule of Load 09:', array09)
print("L09 min on time:", minon09)
print("L09 on time:", np.count_nonzero(array09))
print("L09 max off time:", maxoff09)
print("L09 off time:", 16-np.count_nonzero(array09))

print('Schedule of Load 10:', array10)
print("L10 min on time:", minon10)
print("L10 on time:", np.count_nonzero(array10))
print("L10 max off time:", maxoff10)
print("L10 off time:", 16-np.count_nonzero(array10))

print('Schedule of Load 11:', array11)
print("L11 min on time:", minon11)
print("L11 on time:", np.count_nonzero(array11))
print("L11 max off time:", maxoff11)
print("L11 off time:", 16-np.count_nonzero(array11))

print('Schedule of Load 12:', array12)
print("L12 min on time:", minon12)
print("L12 on time:", np.count_nonzero(array12))
print("L12 max off time:", maxoff12)
print("L12 off time:", 16-np.count_nonzero(array12))

print('Schedule of Load 13:', array13)
print("L13 min on time:", minon13)
print("L13 on time:", np.count_nonzero(array13))
print("L13 max off time:", maxoff13)
print("L13 off time:", 16-np.count_nonzero(array13))

print('Schedule of Load 14:', array14)
print("L14 min on time:", minon14)
print("L14 on time:", np.count_nonzero(array14))
print("L14 max off time:", maxoff14)
print("L14 off time:", 16-np.count_nonzero(array14))

print('Schedule of Load 15:', array15)
print("L15 min on time:", minon15)
print("L15 on time:", np.count_nonzero(array15))
print("L15 max off time:", maxoff15)
print("L15 off time:", 16-np.count_nonzero(array15))

print('Schedule of Load 16:', array16)
print("L16 min on time:", minon16)
print("L16 on time:", np.count_nonzero(array16))
print("L16 max off time:", maxoff16)
print("L16 off time:", 16-np.count_nonzero(array16))

print('Schedule of Load 17:', array17)
print("L17 min on time:", minon17)
print("L17 on time:", np.count_nonzero(array17))
print("L17 max off time:", maxoff17)
print("L17 off time:", 16-np.count_nonzero(array17))

print('Schedule of Load 18:', array18)
print("L18 min on time:", minon18)
print("L18 on time:", np.count_nonzero(array18))
print("L18 max off time:", maxoff18)
print("L18 off time:", 16-np.count_nonzero(array18))

print('Schedule of Load 19:', array19)
print("L19 min on time:", minon19)
print("L19 on time:", np.count_nonzero(array19))
print("L19 max off time:", maxoff19)
print("L19 off time:", 16-np.count_nonzero(array19))

print('Schedule of Load 20:', array20)
print("L20 min on time:", minon20)
print("L20 on time:", np.count_nonzero(array20))
print("L20 max off time:", maxoff20)
print("L20 off time:", 16-np.count_nonzero(array20))

print("\n")








    
