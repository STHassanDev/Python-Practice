import pandas as pd

x={'Student':['David','Samuel','Terry','Evan'],'Age':[27,24,22,32],'County':['UK','Canada','China','USA'],'Course':['Python','Data Structures','Machine Learning','Web Development'],'Marks':[85,72,89,76]}
df = pd.DataFrame(x)
print(type(df[['Student']]))