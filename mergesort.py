import sys

ordered_sets = 0

def mergeSort(array):
    start = 0
    end = len(array)-1
    if start < end:
        middle = int((start + end)/2)
        mid1 = middle
        mid2 = middle+1
        list_1 = mergeSort(array[start:(mid1+1)])
        list_2 = mergeSort(array[mid2:])
        return merge(list_1, list_2)
    else:
        return array

def merge(list1, list2):
    global ordered_sets
    len1 = len(list1)
    len2 = len(list2)
    merged_list = list()
    index1 = index2 = 0
    while index1 < len1 or index2 < len2:
        if index1 < len1 and index2 < len2 and list1[index1] < list2[index2]:
            merged_list.append(list1[index1])
            index1 += 1
        elif index1 < len1 and index2 < len2 and list1[index1] > list2[index2]:
            merged_list.append(list2[index2])
            index2 += 1
            ordered_sets += len1 - index1
        else:
            if index1 < len1:
                merged_list.append(list1[index1])
                index1 += 1
            if index2 < len2:
                merged_list.append(list2[index2])
                index2 += 1
    return merged_list

input_length = int(input())
input_arr = input().split(' ')

for i in range(0, input_length):
	input_arr[i] = int(input_arr[i])

output = mergeSort(input_arr)
print(ordered_sets)