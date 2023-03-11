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