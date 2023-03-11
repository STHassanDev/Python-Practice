def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return arr

def merge_sort(list, start, end): #Takes O(kn logn n) time
    """
    Sorts list in ascending order
    Returns a new sorted list

    Step 1: Find the midpoint of the list and divide into 2 sub lists
    Step 2: Recursively sort the sublists created by step 1
    Step 3> Merge the sorted sublists created in step 2
    """
    
    if start<end:
        mid=(start+(end-1))//2
        merge_sort(list,start,mid)
        merge_sort(list,mid+1,end)
        return merge(list,start,mid,end)

print(merge_sort([3,12,33,66,70,435,42,2 ],0,7))
