import pandas as pd

df = pd.DataFrame({
    "name" : ["John", "Harris", "Catelina", "Allen"],
    "age" : [22,35,34,56],
    "sex" : ["male", "male","female","male"]
})
print(df)
# Column in data frame
print("Age : ")
print(df["age"])
print('--------------------')
df.info()
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    4 non-null      object
 1   age     4 non-null      int64 
 2   sex     4 non-null      object
dtypes: int64(1), object(2)
memory usage: 224.0+ bytes
"""
print('-------------new -------')
# Reading a CSV File
data_set = pd.read_csv("../Data.csv")
print(data_set)
"""
  Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  27.0  48000.0       Yes
2  Germany  30.0  54000.0        No
3    Spain  38.0  61000.0        No
4  Germany  40.0      NaN       Yes
5   France  35.0  58000.0       Yes
6    Spain   NaN  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes
"""
print("---------- head() --------------")
print(data_set.head())
"""
---------- head() --------------
   Country   Age   Salary Purchased
0   France  44.0  72000.0        No
1    Spain  27.0  48000.0       Yes
2  Germany  30.0  54000.0        No
3    Spain  38.0  61000.0        No
4  Germany  40.0      NaN       Yes
"""
print("---------- tail() --------------")
print(data_set.tail())
"""
---------- tail() --------------
   Country   Age   Salary Purchased
5   France  35.0  58000.0       Yes
6    Spain   NaN  52000.0        No
7   France  48.0  79000.0       Yes
8  Germany  50.0  83000.0        No
9   France  37.0  67000.0       Yes
"""
print("---------- head(2) --------------")
print(data_set.head(2))
"""
---------- head(2) --------------
  Country   Age   Salary Purchased
0  France  44.0  72000.0        No
1   Spain  27.0  48000.0       Yes
"""
print(data_set.dtypes)
"""
Country       object
Age          float64
Salary       float64
Purchased     object
dtype: object
"""

