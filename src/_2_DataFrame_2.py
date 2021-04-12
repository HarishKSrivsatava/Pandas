import pandas as pd

housing = pd.read_csv("../housing.csv")
print(housing)
print(housing.head(2))


# subset of a dataframe
print(housing["latitude"].head(3))
print('Type : ', type(housing["latitude"])) # Type :  <class 'pandas.core.series.Series'>
print('Shape of latitude series : ', housing["latitude"].shape) # Shape of latitude series :  (20640,)
print('Shape of housing dataframe : ', housing.shape) # Shape of housing dataframe :  (20640, 10)
print('Size : ', housing["latitude"].size) # Size :  20640

# Accessing multiple columns of a DataFrame
print(housing[["longitude", "longitude"]].head(6))

# filter specific rows from a DataFrame
income = housing[housing["median_income"]<1]
print('Income :\n', income.head(2))

