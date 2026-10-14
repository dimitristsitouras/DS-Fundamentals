import pandas as pd

import numpy as np

df = pd.read_csv(r'week2/Dataset/dirty_data_sample.csv')

print(df)

#So what i did was that at first i ran some diagnostics meaning that I used



df.info()





# >>> df.info()

# <class 'pandas.core.frame.DataFrame'>

# RangeIndex: 6 entries, 0 to 5

# Data columns (total 4 columns):

# # Column Non-Null Count Dtype 

# --- ------ -------------- ----- 

# 0 Name  5 non-null   object 

# 1 Age  5 non-null   object 

# 2 City  5 non-null   object 

# 3 Income 5 non-null   float64

# dtypes: float64(1), object(3)

# memory usage: 324.0+ bytes


df.describe()


# >>> df.describe()

#       Income

# count   5.000000

# mean 64400.000000

# std  14152.738251

# min  49000.000000

# 25%  58000.000000

# 50%  58000.000000

# 75%  72000.000000

# max  85000.000000

# >>> 


df.isnull()


# >>> df.isnull()

#  Name  Age City Income

# 0 False False False False

# 1 False True False False

# 2 False False False  True

# 3 True False False False

# 4 False False True False

# 5 False False False False

# >>> 




df['Income'].sum()



# >>> df['Income'].sum() 

# 322000.0





# Search for Duplicates



df.duplicated()

#### No duplicates were found because for Peter income is null on the 2nd row

# >>> df.duplicated()

# 0  False

# 1  False

# 2  False

# 3  False

# 4  False

# 5  False

# dtype: bool



### Search Data types



df.dtypes



# >>> df.dtypes

# Name   object

# Age    object

# City   object

# Income  float64

# dtype: object

# >>> 



#Τhen I started working on data first I droped what I believed was Peter's duplicate line, then I replaced unknown name and city as "Missing_Name" and , "Missing_City".

#I did not want to drop them because It would still be usefull for many tasks and reports but renamed them for clarity.



#After that I wanted to replace missing ages with the mean of all ages , when I tried to do so I hit anb error because of the value unknown in line 4. So I replaced this value with NaN that I could handle more easily and finally replaced it with the mean.



df_v2 = df.drop(2, axis='rows')

print(df_v2)



### Replace



df_v2['Name'] = df_v2['Name'].fillna("Missing_Name")

df_v2['City'] = df_v2['City'].fillna("Missing_City")

print(df_v2)



df_v2 = df_v2.replace('unknown', np.nan)



df_v2["Age"] = df_v2["Age"].astype(float)

print(df_v2)

df_v2["Age"] = df_v2["Age"].fillna(df_v2["Age"].mean())



final_answer = df_v2



print(final_answer)