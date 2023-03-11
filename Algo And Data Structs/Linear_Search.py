def linear_search(list,target):
    #Return the index position of the target if found, else return None

    for i in range(len(list)):
        if list[i]==target:
            return i
    return None

if __name__=="__main__":
    a = list(int(i) for i in input("Enter some number please: ").strip().split())
    t = int(input("Now Enter the number you wanna find: "))
    print("The target number is a position ",linear_search(a,t))