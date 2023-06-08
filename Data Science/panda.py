import pandas as pd


# Create a dictionary with the data
x = {'Student': ['David', 'Samuel', 'Terry', 'Evan'],
     'Age': [27, 24, 22, 32],
     'County': ['UK', 'Canada', 'China', 'USA'],
     'Course': ['Python', 'Data Structures', 'Machine Learning', 'Web Development'],
     'Marks': [85, 72, 89, 76]}

# Create a DataFrame using the dictionary
df = pd.DataFrame(x)

# Print the type of the DataFrame subset containing the 'Student' column
print(type(df[['Student']]))