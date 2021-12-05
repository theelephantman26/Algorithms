## TESTING CODE : DO NOT EDIT
from random import sample

def find_fixed_point(a, start = 0, end = -1, startFlag = True):
    if startFlag:
        start = 0
        end = len(a)-1
    mid = int((start + end)/2)
    if start < end:
        if a[mid]<mid:
            result = find_fixed_point(a, mid+1, end, False)
        elif a[mid]>mid:
            result = find_fixed_point(a, start, mid-1, False)
        else:
            print('hello', mid)
            return mid
    else:
        if a[mid] == mid:
            print('you', mid)
            return mid
        else:
            return -1
    return result

def find_fixed_point_very_naive(a):
    n = len(a)
    for i in range(0, n):
        if a[i] == i:
            return i
    return -1


def test_find_fixed_point_code(n_tests, test_size):
    n_passed = 0
    for i in range(0, n_tests):
        a = sorted(sample(range(-10 * n_tests, 10 * n_tests), test_size))
        j = find_fixed_point(a)
        k = find_fixed_point_very_naive(a)
        if j != k:
            print(' Code failed for input: ', a, 'returned : ', j, 'expected:', k)
        else:
            n_passed = n_passed + 1

    return n_passed


n_tests = 10000
n_passed = test_find_fixed_point_code(n_tests, 20)
print(' num tests  = ', n_tests)
print(' num passed = ', n_passed)
# END TESTS For find_fixed_point