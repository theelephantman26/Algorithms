def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    i = 0
    j = 0
    merged_list = []
    while i<len(nums1) and j<len(nums2):
        if nums1[i] < nums2[j]:
            merged_list.append(nums1[i])
            i = i + 1
        elif nums1[i] > nums2[j]:
            merged_list.append(nums2[j])
            j = j + 1
        else:
            merged_list.append(nums2[i])
            merged_list.append(nums1[j])
            j = j + 1
            i = i + 1
    if i >= len(nums1) and j < len(nums2):
        while j < len(nums2):
            merged_list.append(nums2[j])
            j = j + 1
    if i >= len(nums1) and j < len(nums2):
        while i < len(nums1):
            merged_list.append(nums1[i])
            i = i + 1
    
    if len(merged_list)%2 is 0:
        mid = int(len(merged_list)/2)-1
        print(merged_list, mid)
        median = (merged_list[mid]+merged_list[mid+1])/2
    else:
        mid = int(len(merged_list)/2)-1
        median = merged_list[mid]
    return median

print(findMedianSortedArrays([1,4,5],[2]))