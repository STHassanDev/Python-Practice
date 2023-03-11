def split(list): #Takes O(k log n) time
    mid= len(list)//2
    return list[:mid], list[mid:]

def merge(left,right): #Takes O(n) time
    """Merges two lists (arrays), sorting thein in the process
    Returns a new merged list
    """
    ans=[]
    i=0
    j=0

    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            ans.append(left[i])
            i+=1
        else:
            ans.append(right[j])
            j+=1

    while i<len(left): #In case the left list is long 
        ans.append(left[i])
        i+=1

    while j<len(right): #In case the right list is long
        ans.append(right[j])
        j+=1
    #here
    return ans


def merge_sort(list): #Takes O(kn logn n) time
    """
    Sorts list in ascending order
    Returns a new sorted list

    Step 1: Find the midpoint of the list and divide into 2 sub lists
    Step 2: Recursively sort the sublists created by step 1
    Step 3> Merge the sorted sublists created in step 2
    """

    if len(list) <=1:
        return list

    left,right = split(list)
    left_list=merge_sort(left)
    right_list=merge_sort(right)

    return merge(left_list,right_list)

print(merge_sort([3,12,33,66,70,435,42,2 ]))
