## test code
## test code: do not edit
from random import randint, sample
import math

def findPointOfIntersection(xValues, yValues, start = 0, end = -1, startFlag = True):
    # Your CODE HERE
    # ....
    if startFlag:
        end = len(xValues)-1
    mid1 = math.floor((start+end)/2)
    mid2 = mid1 + 1
    if start < end:
        if xValues[mid1] > yValues[mid1] and xValues[mid2] > yValues[mid2]:
            point = findPointOfIntersection(xValues, yValues, start, mid1, False)
        elif xValues[mid1] < yValues[mid1] and xValues[mid2] < yValues[mid2]:
            point = findPointOfIntersection(xValues, yValues, mid2, end, False)
        else:
            return mid1
    else:
        if xValues[mid1] > yValues[mid1] and xValues[mid2] < yValues[mid2]:
            return mid1
        else:
            return -1
    return point

def checkIntersection(xValues, yValues, i):
    if (i < 0 or i >= len(xValues)):
        return False
    if (xValues[i] < yValues[i] and xValues[i+1] > yValues[i+1]):
        return True
    return False

def isOK(xValues, yValues):
    n = len(xValues)
    assert (len(yValues) == n)
    if (xValues[0] >= yValues[0]):
        return False
    if (xValues[n-1] <= yValues[n-1]):
        return False
    for i in range(n):
        if (xValues[i] == yValues[i]):
            return False
        if (i < n-1 and xValues[i+1] <= xValues[i]):
            return False
        if (i < n-1 and yValues[i+1] <= yValues[i]):
            return False
    return True



xValues1 = [-4, -1, 2, 3, 5, 7, 9]
yValues1 = [ 0, 2, 3, 3.5, 4, 5, 7]
j1 = findPointOfIntersection(xValues1, yValues1)
print('j1 = ', j1)
assert checkIntersection(xValues1, yValues1, j1)

xValues2 = [-5, -4, -3, -2, -1, 0, 5, 10, 15, 20, 25]
yValues2 = [ 0,  2, 4,  8, 10, 12, 14, 16, 18, 19, 22]
j2 = findPointOfIntersection(xValues2, yValues2)
print('j2 = ', j2)
assert checkIntersection(xValues2, yValues2, j2)



xValues3 = [-2, -1, 0, 1, 2]
yValues3 = [ 0, 0.5, 1, 1.5, 1.75]
j3 = findPointOfIntersection(xValues3, yValues3)
print('j3 = ', j3)
assert checkIntersection(xValues3, yValues3, j3)



xValues4 = [-2, 2]
yValues4 = [ 0, 1 ]
j4 = findPointOfIntersection(xValues4, yValues4)
print('j4 = ', j4)
assert checkIntersection(xValues4, yValues4, j4)




def testPointOfIntersection(size, numTrials):
    numActual = 0
    for j in range(numTrials):
        yValues = list(range(size))
        k = randint(1,size-2)
        xValues = []
        for i in range(k):
            xValues.append(yValues[i] - 2)
        for i in range(k, size):
            xValues.append(yValues[i] + 2)
        #print(xValues, yValues)
        if (isOK(xValues, yValues)):
            j = findPointOfIntersection(xValues, yValues)
            numActual = numActual + 1
            if (not checkIntersection(xValues, yValues, j)):
                print("--- FAILED TEST -- ")
                print("xValues:", xValues)
                print("yValues:", yValues)
                print("Your code returned:", j)
                print("--- End Fail Report -- ")
                return False
    print("All %d tests passed"%numActual)
    return True

testPointOfIntersection(50, 100)
testPointOfIntersection(75, 100)
# end Test Code
