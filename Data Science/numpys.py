import numpy as np

# A traditional python list can store different data types in the same list. This is possible through dynamic resizing.
a = [False, 1, "two", "3", 4.00]

# Creates a numpy array
b = np.array([1,2,3,4,5])

print(type(a),'\n',type(b))

b.dtype # Returns the data type of the elements stored in the array. In this case: 'int32'

"""
Elements in a numpy array can be accessed in the same matter as traditional python lists.
Example: 
b[0] will give 1
b[1] will give 2
etc...
"""
for i in range(len(b)): # Numpy arrays can also use the len() function
    print(b[i])

a[[0,2,4,]] # We can pass a list of integers to select multiple indexes at once. 

"""
Numpy arrays can be sliced as well. The syntax resembles that of the range function. 
b[2:4] -> array([3, 4]) # This will return the third and fourth elements in the array. 
Notice how the fifth is excluded. Just like the range function, the end bound is excluded.

We can also define the steps in slicing by including a third number as the parameter.

b[0::2] -> array([1,3,5])   # This will return every OTHER element in the array starting with the first 
""" 

c = b[:5] # This will create a list containing every element in b except the last one. 
#The program will assume 0 as the start bound and -1 as the end bound if a number is not passed.


