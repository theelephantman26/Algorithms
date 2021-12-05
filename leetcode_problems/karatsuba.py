def addLists(list1, list2):
    num1 = ''.join([str(i) for i in list1])
    num2 = ''.join([str(i) for i in list2])
    return [int(item) for item in list(str(int(num1) + int(num2)))]

def subtractLists(list1, list2):
    num1 = ''.join([str(i) for i in list1])
    num2 = ''.join([str(i) for i in list2])
    return [int(item) for item in list(str(int(num1) - int(num2)))]

def normalize

def karatsubaMul(num1, num2, start, end):
    mid = int((start + end)/2)
    if start == end:
        return [int(item) for item in list(str(num1[start]*num2[start]))]
    else:
        p0 = karatsubaMul(num1[start:mid], num2[start:mid], start, mid)

        t1 = addLists(num1[start:mid], num1[(mid+1):end])
        t2 = addLists(num2[start:mid], num2[(mid+1):end])
        p1 = karatsubaMul(t1, t2, 0, len())
        p2 = karatsubaMul(num1[(mid+1):end], num2[(mid+1):end], mid+1, end)
        return p2 + subtractLists(subtractLists(p1, p0), p2) + p0

num1 = [int(i) for i in list('123456789')]
num2 = [int(i) for i in list('123456789')]
if len(num1) > len(num2):
    for i in range(0, len(num1) - len(num2)):
        num1.insert(0, 0)

if len(num2) > len(num1):
    for i in range(0, len(num2) - len(num1)):
        num1.insert(0, 0)

print(karatsubaMul(num1, num2, start, end))
