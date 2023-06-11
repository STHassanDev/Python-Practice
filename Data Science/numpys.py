import numpy as np

# A traditional Python list can store different data types in the same list due to dynamic resizing.
a = [False, 1, "two", "3", 4.00]

# Creates a NumPy array
b = np.array([1, 2, 3, 4, 5])

print(type(a), '\n', type(b))

b.dtype  # Returns the data type of the elements stored in the array. In this case: 'int32'

"""
Elements in a NumPy array can be accessed similarly to traditional Python lists.
Example: 
b[0] will give 1
b[1] will give 2
etc...
"""
for i in range(len(b)):  # NumPy arrays can also use the len() function
    print(b[i])

a[[0, 2, 4]]  # We can pass a list of integers to select multiple indexes at once.

"""
NumPy arrays can be sliced as well. The syntax resembles that of the range function. 
b[2:4] -> array([3, 4])  # This will return the third and fourth elements in the array. 
Notice how the fifth element is excluded. Similar to the range function, the end bound is excluded.

We can also define the steps in slicing by including a third number as the parameter.

b[0::2] -> array([1, 3, 5])  # This will return every OTHER element in the array starting with the first 
"""

c = b[:5]  # This will create a new array containing every element in b except the last one. 
# If a number is not passed, the program assumes 0 as the start bound and -1 as the end bound.