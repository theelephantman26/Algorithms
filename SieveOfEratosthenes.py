print('Enter the upper limit')
till = int(input())
num_range = range(1, till+1)
numbers = list(num_range)
numbers[numbers.index(1)] = -1
primes = list()
primes.append(1)
for num in num_range:
    if num in numbers and numbers[numbers.index(num)] != -1:
        primes.append(num)
        for j in num_range[1:]:
            multiple = num*j
            if multiple in numbers and multiple <= till:
                numbers[numbers.index(multiple)] = -1
    else:
        continue
print(primes)