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