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

def recursive_binary_search(list,target):
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
    a = list(int(i) for i in input("Enter some numbers please: ").strip().split())
    t = int(input("Now Enter the number you wanna find: "))
    print("The target number is a position ",recursive_binary_search(a,t))

# This is a recursive version Binary Search runs at O(log n) and uses O(log n) space.

# Python has a recursive depths so dont use recursion often.