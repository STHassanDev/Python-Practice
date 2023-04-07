
def openf(filename): #Loads the contents in a file into a list with each element representing a line of text
    ans = []
    with open(filename,"r") as f:
        for line in f:
            ans.append(f.readline())
        
    return ans

openf(input())