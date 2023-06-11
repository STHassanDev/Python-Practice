#import pandas as pd


# Create a dictionary with the data
x = {'Student': ['David', 'Samuel', 'Terry', 'Evan', 'Kyoko'],
     'Age': [27, 24, 22, 32, 23],
     'Country': ['UK', 'Canada', 'China', 'USA', 'Japan'],
     'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development', 'Cryptography'],
     'Marks': [85, 72, 89, 76, 91]}

    
# Create a DataFrame using the dictionary
df = pd.DataFrame(x)
print(df)
print(type(df),'\n')

# Retrieving the "Course" column and assigning it to variable a
a = df[["Course"]]
print(a)
print(type(a),'\n')

# Retrieing the Student, Age and Country columns and assigning all three to variable b
b = df[["Student","Age","Country"]]
print (b)
print(type(b),'\n')

"""
The Pandas library contains two primary functions for data selecting loc() and iloc 

loc() uses the LABELS of the rows and columns as the parameters
- Rows or columns with no labels must be referenced through their indexes

iloc() uses the INDEXES of the rows and columns as the parameters
"""

# Access the value on the first row and the first column 
d = df.iloc[0,0]

# Access the value on the first row and the third column
dc = df.loc[0,"Country"]

# Access the value on the third row and the first column
t = df.iloc[2,0]

# Access the value on the third row and the third column
tc = df.loc[2,"Country"]

print(d,' lives in ',dc)
print(t," lives in ",tc)

"""
In order to get rid of the index column of the dataframe, we use the set_index() method to 
set one of the pre exisitng columns as the "index" for both the iloc() and the loc() methods.
Notice how since we are setting the "Student" columnn as the index, we can no longer use the 
zero index to retrieve names from the data frame.
"""

print('\n')

df2 = df
df2 = df2.set_index("Student")

# This method displays the first 5 rows of the dataframe (In this case, it will display the entire data frame)
print(df2.head())



s = df2.iloc[1,0] 
e = df2.iloc[3,0]
"""
 Previously these would have retrieved the name from the "Student" column but it now retrieves 
the age instead.
"""

print('\n')

# Access the value on the second row and the third column
sc = df2.loc['Samuel',"Country"]

# Access the value on the fourth row and the third column
ec = df2.loc['Evan',"Country"]

print("Samuel lives in ",sc,"and is",s,'years old')
print("Evan lives in ",ec,"and is",e,'years old')

"""
The loc() method can also be used to slice a DataFrame or Series based on the labels of rows and columns.
It is inclusive of both the start and end bounds.

Syntax: df.loc[row_label_start : row_label_end, column_label_start : column_label_end]
"""
 
# Example:
print(df.loc[1:4, 'Student':'Country'])  # Selects rows 1 to 4 (inclusive) and columns 'Student' to 'Country' (inclusive).

# Note that the labels can be integers or strings, depending on the index type.

""" The `iloc()` method is used to slice a DataFrame or Series based on the integer positions of rows and columns.
 It is inclusive of the start bound and exclusive of the end bound.

 Syntax: df.iloc[row_position_start:row_position_end, column_position_start:column_position_end]
"""
# Example:
print(df.iloc[0:4, 0:3])  # Selects rows 2 to 4 (exclusive of row 5) and columns 0 to 2 (exclusive of column 3).


