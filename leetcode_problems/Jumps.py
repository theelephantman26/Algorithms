from math import inf
def Jumps(nums):
    largestJump = len(nums)
    visited = [False]*largestJump
    distance = [inf]*largestJump
    distance[0] = 0
    i = 0
    while not visited[largestJump-1] and i<largestJump:
        for j in range(nums[i],0,-1):
            print(i, j, i+j)
            if i+j > largestJump-1:
                continue
            if not visited[i+j]:
                visited[i+j]= True
                distance[i+j] = distance[i]+1
            else:
                break
            if visited[largestJump-1]:
                print(distance)
                return distance[i+j]
        i=i+1
    return distance[largestJump-1]
# [1,2,1,1,1], [1,2,3,4,5]
nums = [2,3,1,5,4,1,1,1,1,1,5]
print(Jumps(nums))