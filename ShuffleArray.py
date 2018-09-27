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

def shuffleArrayBubbleSort(a):
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


array = list(range(1,31))
print(shuffleArrayBubbleSort(array))
