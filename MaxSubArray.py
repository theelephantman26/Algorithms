import math
def maxSubArray(a):
    # Code here.
    # Just use a single for loop that iterates over
    # the array in forward or reverse direction, as you please
    ans_i = i = 0
    ans_j = j = 1
    diff = -1*math.inf
    while j < len(a):
        if a[j] < a[i]:
            i = j
        else:
            if a[j]-a[i] > diff:
                ans_i = i
                ans_j = j
                diff = a[ans_j] - a[ans_i]
        j = j+1
    return diff

# test 1
from random import sample

a = [3, 1, 0, 3, 2, 1, 4, 9, 10, 8, 5, 7, 9]
# print(maxSubArray(a))
assert maxSubArray(a) == 10, 'Test 1 failed'

# test 2

b = [10, 4, 5, 1, 2, 7, 8, 1, 0, -10, 10, -5, 19, 231, 11, -55]
# print(maxSubArray(b))
assert maxSubArray(b) == 241, 'Test 2 failed'

# test 3

c = [10, 2, -1, -5, -4]

# print(maxSubArray(c))
assert maxSubArray(c) == 1, 'Test 3 failed'


# test 4

def naiveMaxSubArray(a):
    n = len(a)
    maxSoFar = -math.inf
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] < a[j] and maxSoFar < (a[j] - a[i])):
                maxSoFar = a[j] - a[i]
    return maxSoFar


def testMaxSubArray(nTests, testSize):
    for i in range(nTests):
        a = sample(range(-1 * nTests, nTests), testSize)
        j = naiveMaxSubArray(a)
        l = maxSubArray(a)
        if (j != l):
            print('Failed for array: ', (a), '\n Expected: ', j, ' Obtained: ', l)
            return
    print(nTests, 'tests passed!')


testMaxSubArray(1000, 5)
testMaxSubArray(1000, 10)
testMaxSubArray(1000, 30)