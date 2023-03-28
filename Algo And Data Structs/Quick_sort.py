import sys

def quick_sort(values):
    """ Selects the first elements in the array as the 'pivot'. Creates two sublists with one 
    representing the elements less than the pivot and the other representing the elements greater than
    the pivot. Recursively repeats this process for the sublists until we are left with empty lists or
    single elements lists. Adds the list together to form the sorted array.
    """
    if len(values)<=1:
        return values
    less = [] #sublist of all elements less than or equal to the pivot
    great = [] #sublist of all elements greater than the pivot
    pivot = values[0]
    for i in values[1:]:
        if i <= pivot:
            less.append(i)
        else:
            great.append(i)
    return quick_sort(less) + [pivot] + quick_sort(great)

print (quick_sort([2,5,3,1,9,7,8,65,34,68,32,11]))