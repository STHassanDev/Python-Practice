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

b[[0, 2, 4]]  # We can pass a list of integers to select multiple indexes at once.

"""
NumPy arrays can be sliced as well. The syntax resembles that of the range function. 
b[2:4] -> array([3, 4])  # This will return the third and fourth elements in the array. 
Notice how the fifth element is excluded. Similar to the range function, the end bound is excluded.

We can also define the steps in slicing by including a third number as the parameter.

b[0::2] -> array([1, 3, 5])  # This will return every OTHER element in the array starting with the first 
"""

c = b[:5]  # This will create a new array containing every element in b except the last one. 
# If a number is not passed, the program assumes 0 as the start bound and -1 as the end bound.

"""
When accessing elements in the array using indexing, Numpy allows you to pass a list of numbers
as a parameter. 
Example
b[[1,2,3]]
This will return a list containing the elements in the corresponding indices.
"""
print(b[[1,2,3]])

### Numpy Statistical Functions

b.mean() # Returns the average value of the values in the array

b.std() # Returns the standard deviation of the values in the array

# Returns the minimum and maximum values of the array respectively
b.min()
b.max() 

### Numpy Array Operations ( NOTE  THESE OPERATIONS ONLY WORK WITH ARRAYS OF THE SAME LENGTH)

c = np.array([1,2,3,4,5])

w = np.add(b, c) # Returns an array of the sums of each element in the arrays. 
# Can also be written as:
b+c

x = np.subtract(b,c) # Returns an array of the differences of each element in the arrays. 
# Can also be written as:
b-c 

y = np.multiply(b,c) # Returns an array of the products of each element in the arrays.
# Can also be written as:
b*c

z = np.divide(b,c) # Return an array of the quotients of each element in the arrays. 
# (Note that the quotients are represents as floats)
# Can also be written as:
b/c

XYZ = np.dot(b,c) # Returns the SUM of the products of each element in the arrays.


"""
NumPy can also handle pi and the standard trig functions.
np.pi -> Returns a float representing pi
np.sin(x) -> Returns the sine of each element in the array.
np.cos(x) -> Returns the cosine of each element in the array.
np.tan(x) -> Returns the tangent of each element in the array.
"""

# LineSpace is a function that returns an array containing evenly spaced numbers over a specified interval
np.linspace(1,10,20)
"""
First parameter is the start bound
Second parameter is the end bound
Third parameter is the number of values to generate.
"""