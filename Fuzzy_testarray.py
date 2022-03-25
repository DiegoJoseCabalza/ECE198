import numpy as np

##checker for count 1's in array

#arr = np.array([False, True, True, True, False, True, False, True, True])
arr = np.array([0, 2, 1, 1, 0, 1, 0, 1, 1])
print('Numpy Array:', arr)
# Get count of True elements in a numpy array
count = np.count_nonzero(arr)
print('Print count of True elements in array: ', count)

maxvalue = np.nanmax(arr)
print('max', maxvalue)

totalpenalty = 0
while (totalpenalty<5):
    totalpenalty +=1
    print(totalpenalty)
