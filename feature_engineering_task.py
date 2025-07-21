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
    'Grade': ['A', 'B', 'C', 'B', 'A']
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



#output

After Adding Total & Average:
       Name  Total    Average
0    princr    248  82.666667
1  priyansh    231  77.000000
2     sahil    228  76.000000
3    gautam    219  73.000000
4     rahul    221  73.666667

 After Encoding:
       Name Gender  Gender_code Grade  Grade_code
0    princr      M            1     A           0
1  priyansh      M            1     B           1
2     sahil      M            1     C           2
3    gautam      M            1     B           1
4     rahul      M            1     A           0

After Handling Missing Values:
       Name  Math  Science  English  ... Total    Average  Gender_code  Grade_code
0    princr    84       86       78  ...   248  82.666667            1           0
1  priyansh    68       82       81  ...   231  77.000000            1           1
2     sahil    88       69       71  ...   228  76.000000            1           2
3    gautam    76       76       67  ...   219  73.000000            1           1
4     rahul    67       66       88  ...   221  73.666667            1           0

[5 rows x 10 columns]

After MinMax Scaling:
       Name  Math  Math_Scaled
0    princr    84     0.809524
1  priyansh    68     0.047619
2     sahil    88     1.000000
3    gautam    76     0.428571
4     rahul    67     0.000000

 After Standard Scaling: 
       Name      Math   Science   English
0    princr  0.882957  1.351497  0.135086
1  priyansh -1.026139  0.821498  0.540343
2     sahil  1.360231 -0.900998 -0.810515
3    gautam -0.071591  0.026500 -1.350858
4     rahul -1.145458 -1.298497  1.485944
