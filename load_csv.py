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
