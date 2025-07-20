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

# Pie chart displays percentage of each flower species
plt.figure(figsize=(6, 6))
species_counts = df['species'].value_counts()

plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title("Species Distribution in Iris Dataset", fontsize=14)
plt.tight_layout()
plt.show()
