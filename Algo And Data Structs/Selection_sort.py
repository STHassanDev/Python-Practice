import sys

def selection_sort(values):
    min=values[0]
    sort=[]
    
    for i in range(1,len(values)):
        if values[min]>values[i]:
            min=i
    sort.append(values.pop(min))



