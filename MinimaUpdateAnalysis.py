import math
import random
import matplotlib as plt
import tensorflow as tf

def updates(a):
    min_so_far = math.inf
    number_updates = 0
    for element in a:
        if element < min_so_far:
            min_so_far = element
            number_updates = number_updates + 1
    return number_updates

# array = list(range(1,100))
# total_updates = list()
# for i in range(0, 100):
#     random.shuffle(array)
#     total_updates.append(updates(array))
#     print(i)
# print(total_updates.count(3))
#
# plt.plot([i for i in range(0, 101)], [total_updates.count(i) for i in range(0, 101)])
# plt.show()

print(tf.__version__)