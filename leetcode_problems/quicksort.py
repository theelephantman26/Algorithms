from random import randint

def quicksort(array, low, high):
    if low < high:
        array, pdx = partition(array, low, high)
        array = quicksort(array, low, pdx-1)
        array = quicksort(array, pdx+1, high)
    return array
        
def partition(array, low, high):
    pdx = high
    pivot = array[pdx]
    i = low
    for j in range(low, high+1):
        if array[j] <= pivot:
            array[j], array[i] = array[i], array[j]
            i = i+1
    return array, i-1

array = [11, 10, 1,9, 8, 2, 5, 7]
print(quicksort(array, 0, len(array)-1))