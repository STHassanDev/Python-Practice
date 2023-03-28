import sys

def selection_sort(values):
    sort=[]
    for j in range(0,len(values)):
        min = 0
        for i in range(1,len(values)):
            if values[i] < values[min]:
                min = i
        sort.append(values.pop(min))
    return sort
    
print(selection_sort([1,5,3,9,4,3,2,9,23,43,11,12,13]))

