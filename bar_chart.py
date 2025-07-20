# sklearn (Iris dataset)

from sklearn.datasets import load_iris  # For loading the Iris dataset
import pandas as pd                     
import matplotlib.pyplot as plt        
import seaborn as sns                   


iris = load_iris()  

df = pd.DataFrame(iris.data, columns=iris.feature_names)


df['species'] = iris.target

df['species'] = df['species'].map({
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
})


print(df.head())  

sns.set(style="whitegrid")  


plt.figure(figsize=(8, 5))  # Set the size of the figure
sns.countplot(data=df, x='species', palette='Set2') 

plt.title(" Count of Each Iris Species", fontsize=14)
plt.xlabel("Flower Species")
plt.ylabel("Number of Samples")

# Clean up layout and display the plot
plt.tight_layout()
plt.show()
