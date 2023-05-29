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

def binary_search(list,target):
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

if __name__=="__main__":
    a = list(int(i) for i in input("Enter some number please: ").strip().split())
    t = int(input("Now Enter the number you wanna find: "))
    print("The target number is a position ",binary_search(a,t))

# This iterative version of Binary Search runs at O(log n) time and uses O(1) space