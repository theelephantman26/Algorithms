from random import randint
def simulateCouponCollection(n):
    # Your code here.
    b = [False]*(n)
    count = 0
    while not all(item for item in b):
        b[randint(0,n-1)] = True
        count = count+1
    return count

def runCouponCollectionExperiment(nMax):
    returnData = {}
    for n in range(10, nMax+1, 10):
        coupons = list()
        count = 0
        while count <=1000:
            coupons.append(simulateCouponCollection(n))
            count = count+1
        returnData[n] = sum(coupons)/len(coupons)
    return returnData

mymap = runCouponCollectionExperiment(20)
print(mymap)