import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

print(" Dataset Info:\n")
print(df.info())

print("\n Missing Values in Each Column:\n")
print(df.isnull().sum())

print("\n Basic Statistical Summary:\n")
print(df.describe())

print("\n Data Types:\n")
print(df.dtypes)

print("\n First 5 Rows of Data:\n")
print(df.head())


print("\n Survival Rate by Gender:\n")
print(df.groupby('Sex')['Survived'].mean())


print("\n Average Age by Pclass:\n")
print(df.groupby('Pclass')['Age'].mean())
