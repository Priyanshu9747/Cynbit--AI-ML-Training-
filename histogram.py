
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print(df.head())

#Histogram shows how petal length is distributed 
plt.figure(figsize=(8, 5))
sns.histplot(df['petal length (cm)'], bins=20, kde=True, color='skyblue')

plt.title("Distribution of Petal Length", fontsize=14)
plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.show()
