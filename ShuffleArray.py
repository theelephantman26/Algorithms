from random import getrandbits
import math

def generateRandomIndex(bits):
    number = 0
    for i in range(bits):
        number = number*2 + getrandbits(1)
    return number

def shuffleArray(a):
    shuffled_list = a.copy()
    all_elements_shuffled = [False]*len(a)
    taken = [False]*len(a)
    bits = math.ceil(math.log(30,2))
    for i in range(len(a)):
        shuffled = False
        while not shuffled:
            index = math.inf
            while index >= len(a):
                index = generateRandomIndex(bits)
            if taken[index] is False:
                shuffled_list[index] = a[i]
                shuffled = True
                taken[index] = True
    return shuffled_list

def shuffleArrayAppendToLists(a):
    array_copy = a.copy()
    shuffled_list = list()
    for i in range(0, len(a)):
        index = math.inf
        bits = math.ceil(math.log(len(array_copy),2))
        while index >= len(array_copy):
            index = generateRandomIndex(bits)
        shuffled_list.append(array_copy[index])
        del(array_copy[index])
    return shuffled_list

def shuffleArrayPriorities(a):
    shuffled_array = list()
    priorities = list()
    bits = math.ceil(math.log(len(a),2))
    priority_to_index = {}
    used_priorities = list()
    for i in range(0, len(a)):
        priority = math.inf
        while True:
            priority = generateRandomIndex(bits)
            if priority < len(a) and priority not in used_priorities:
                break
        used_priorities.append(priority)
        priority_to_index[priority] = a[i]
    for i in range(0, len(a)):
        shuffled_array.append(priority_to_index[i])
    return shuffled_array

def shuffleArrayQuickSort(array, start=0, end=-1, startFlag = True):
    if startFlag:
        start = 0
        end = len(array)-1
    if start < end:
        p = partition(array, start, end)
        shuffleArrayQuickSort(array, start, p-1, False)
        shuffleArrayQuickSort(array, p+1, end, False)
    return array

def partition(array, start, end):
    pivot = array[end]
    i = start
    for j in range(start, end, 1):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i = i+1
    array[i], array[end] = array[end], array[i]
    return i

def shuffleArrayQuickUnsort(array, start=0, end=-1, startFlag = True):
    if startFlag:
        start = 0
        end = len(array)-1

    if start < end:
        bits = math.ceil(math.log(end-start+1,2))
        p_index = math.inf
        while p_index < start or p_index > end:
            p_index = start + generateRandomIndex(bits)
        shuffleArrayQuickUnsort(array, start, p_index-1, False)
        shuffleArrayQuickUnsort(array, p_index+1, end, False)
        partitionUnsort(array, start, end, p_index)
    return array

def partitionUnsort(array, start, end, p_index):
    pivot = array[p_index]
    i = p_index
    array[i], array[end] = array[end], array[i]
    for j in range(end-1, start-1, -1):
        if array[j] > pivot:
            array[j], array[i] = array[i], array[j]
            i = i-1


array = list(range(11))
print(shuffleArrayQuickUnsort(array))
