import pandas as pd

# Load CSV file from a URL or local path
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Show statistical summary of numerical columns
print("\nStatistical Summary:")
print(df.describe())

print(df['Survived'].value_counts())

print(df.groupby('Sex')['Survived'].mean())

print(df.isnull().sum())

df = df.dropna(subset=['Age'])

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
