import pandas as pd

# Titanic dataset
titanic = pd.read_csv("../titanic.csv")
print(titanic.describe())
print(titanic.info())
print(titanic["Pclass"].head(2))
#print(titanic)

# titanic passengers from cabin class 2 and 3
classPass = titanic[titanic["Pclass"].isin([2,3])]
print('Class Passengers : \n', classPass.head(6))
"""
Class Passengers : 
    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
2            3         1       3  ...   7.9250   NaN         S
4            5         0       3  ...   8.0500   NaN         S
5            6         0       3  ...   8.4583   NaN         Q
7            8         0       3  ...  21.0750   NaN         S
8            9         1       3  ...  11.1333   NaN         S
"""

classPass2 = titanic[(titanic["Pclass"] == 2)  | (titanic["Pclass"] == 3)]
print('Class Passengers 2 : \n', classPass2.head(6))
"""
Class Passengers 2 : 
    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
0            1         0       3  ...   7.2500   NaN         S
2            3         1       3  ...   7.9250   NaN         S
4            5         0       3  ...   8.0500   NaN         S
5            6         0       3  ...   8.4583   NaN         Q
7            8         0       3  ...  21.0750   NaN         S
8            9         1       3  ...  11.1333   NaN         S
"""

# passenger data for which the age is known
print('Age : ', titanic["Age"])
# notna() conditional function returns a True for each row the values are not an Null value
passengerWithAge = titanic[titanic["Age"].notna()]
print('Dataframe shape : ', titanic.shape) # Dataframe shape :  (891, 12)
print('Passage shape : ', passengerWithAge.shape) # Passage shape :  (714, 12)


# specific rows and columns from a DataFrame
# names of the passengers older than 35 years

age_passengers = titanic[titanic["Age"] > 35]
print(age_passengers)

