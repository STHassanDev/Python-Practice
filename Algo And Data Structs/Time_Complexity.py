from timeit import timeit

def linear_search(list,target):
    #Return the index position of the target if found, else return None

    for i in range(len(list)):
        if list[i]==target:
            return i
    return None

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
    a=[1,2,3,4,5,6,7,8,9,10]
    start=timeit()
    recursive_binary_search([1,2,3,4,5,6,7,8,9,10],8)
    end=timeit()
    print(end-start)