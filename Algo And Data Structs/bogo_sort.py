import random
import sys

def is_sorted(values):
    for index in range(len(values)-1):
        if values[index]>values[index+1]:
            return False
    return True

def bogo_sort(values): #Random shuffles list until it is sorted. One of the lest effective algorithms
    attempt=0
    while not is_sorted(values):
        random.shuffle(values)
        attempt+=1
    print(attempt)
    return values

print(bogo_sort([1,4,2,3,6,8,7,9]))
