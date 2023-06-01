

new_list=[1,2,3,4,5,6,7]
new_list[10] 
#Will access in constant time HOWEVER it will crash because index is out of range

if 5 in new_list: print(True) 
# O(n) runtime bc of "in" operator.Uses contains function from list

# Three different types of insert for a list. 
#Insert O(n) runtime
new_list.insert(3,11) # At index 3 insert 11. 

#Append O(1) runtime
new_list.append(13) # Add 13 to the END of the list.

#Extend O(k) where k depends on the input size
new_list.extend([34,56,75]) # Adds the input list to the orginal list. 
#Extend is essentially a series of append calls.

"""When an insert method is called and the list is out of space, the resize function
is called. All three methods have an ammortized constant space complexity. Meaning they
resize after a certain amount of inserts. The sequence for the python is 
0,4,8,16,25,35,46..."""

# Delete operates in a similiar way to insert but in reverse. The index of each 
# element shifts meaning a linear runtime. 

new_list.remove(1) # Specify the number O(n)

new_list.pop(3) # Specify the index O(n)

new_list.pop() # Calls .pop(-1) O(1)


