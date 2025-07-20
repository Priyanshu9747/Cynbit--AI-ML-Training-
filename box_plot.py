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

plt.figure(figsize=(8, 5))
sns.boxplot(x='species', y='sepal width (cm)', data=df, palette='Set3')

plt.title("Spread of Sepal Width by Species", fontsize=14)
plt.xlabel("Species")
plt.ylabel("Sepal Width (cm)")
plt.tight_layout()
plt.show()
