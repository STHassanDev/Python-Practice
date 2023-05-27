from timeit import timeit

""" 
The following three functions return the index position of the target if found, else return None
Both binary search and recursive binary search assume the list is sorted before searching through it.
"""

def linear_search(list,target): 
    """
    This function iterates over an array and returns the index of the first appearance of the target value. 
    Linear Search is one of the most standard types of search. 
    It has a runtime of O(n)
    """
    for i in range(len(list)):
        if list[i]==target:
            return i
    return None

def binary_search(list,target):
    """
    The list input must already be sorted before calling this function.
    This function uses the divide and conquer approach to searching by using two references to 
    the first and last indexes. 
    Compares the median value to the target value:
        - If they are the same: return the median index
        - If the target is less than the median: redefine the last index and search the second half of the list
        - If the target is more than the median: redefine the first index and search the first half of the list
    Since the list is cut in half with each iteration:
    This function has a runtime of O(log n)
    """

    first=0
    last=len(list)-1
    
    while first<=last:
        mid=(first+last)//2
        if list[mid]==target:
            return mid
        elif list[mid]<target:
            first=mid+1
        else:
            last=mid-1
    return None

def recursive_binary_search(list,target):
    """
    The list input must already be sorted before calling this function.
    This function uses the same divide and conquer approach as binary search but instead of referencing the first 
    and last indexes, it uses recursion to call itself.
    Compares the median value to the target value:
        - If they are the same: return the median index
        - If the target is less than the median: call the function again using the second half of the list as an input.
        - If the target is more than the median: call the function again using the first half of the list as an input.
    Since the list is still being cut in half with each iteration:
    This function also has a runtime of O(log n)
    """

    if len(list)==0:
        return None
    else:
        mid=len(list)//2
        if list[mid]==target:
            return mid
        else:
            if list[mid]<target:
                return recursive_binary_search(list[mid+1:],target)
            else: 
                return recursive_binary_search(list[:mid],target)
            
if __name__=="__main__":
    a=[1,2,3,4,5,6,7,8,9,10]
    start=timeit()
    recursive_binary_search([1,2,3,4,5,6,7,8,9,10],8)
    end=timeit()
    print(end-start)