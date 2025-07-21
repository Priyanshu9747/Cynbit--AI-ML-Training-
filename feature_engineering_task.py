import pandas as pd
from sklearn.preprocessing import LabelEncoder,MinMaxScaler,StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['princr', 'priyansh', 'sahil', 'gautam', 'rahul'],
    'Math': [84, 68, 88, 76, 67],
    'Science': [86, 82, 69, 76, 66],
    'English': [78, 81, 71, 67, 88],
    'Gender': ['M', 'M', 'M', 'M', 'M'],
    'Grade': ['A', 'B', 'A', 'C', 'B']
}
df=pd.DataFrame(data)

#create new columns for existing ones
df['Total'] = df[['Math', 'Science', 'English']].sum(axis=1, min_count=2)  # At least 2 subjects present
df['Average'] = df['Total'] / 3
print("\nAfter Adding Total & Average:")
print(df[['Name', 'Total', 'Average']])


#Encode categorical data (covert text to numbers):

df["Gender_code"]=df["Gender"].map({"M":1,"F":0})
#le = label encoder 
le = LabelEncoder()
df["Grade_code"] = le.fit_transform(df["Grade"].fillna("Unknown"))

print("\n After Encoding:")
print(df[["Name","Gender","Gender_code","Grade","Grade_code"]])

# Handle missing values:
df['Math'].fillna(df['Math'].mean(), inplace=True)
df['Science'].fillna(df['Science'].mean(), inplace=True)
df['English'].fillna(df['English'].mean(), inplace=True)

# Drop rows with missing grades (optional)
df.dropna(subset=['Grade'], inplace=True)

print("\nAfter Handling Missing Values:")
print(df)

#Correlation Matrix (find the hidden relationship):
corr = df[['Math', 'Science', 'English', 'Total', 'Average']].corr()

# Visualize
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title("Subject Correlation Heatmap")
plt.show()

#normalization (use minmax_scaler and standard_scaler):
scaler = MinMaxScaler()
df[['Math_Scaled']] = scaler.fit_transform(df[['Math']])

print("\nAfter MinMax Scaling:")
print(df[['Name', 'Math', 'Math_Scaled']])

scaler = StandardScaler()

# Scale numerical columns
numeric_cols = ['Math', 'Science', 'English']
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("\n After Standard Scaling: ")
print(df[['Name', 'Math', 'Science', 'English']])