import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris # type: ignore
import seaborn as sns

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris. feature_names)
df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})
df.head()
print(df.info())
print(df.isnull().sum())
df.describe()
df.groupby('species').mean()
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['sepal length (cm)'], label="Sepal Length", color='b')
plt.plot(df.index, df['petal length (cm)'], label="Petal Length", color='r')
plt.xlabel("Index")
plt.ylabel("Length (cm)")
plt.title("Trends in Sepal and Petal Length")
plt.legend()
plt.show()
plt.figure(figsize=(8, 5))
sns.barplot(x='species', y='petal length (cm)', data=df)
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()
plt.figure(figsize=(8, 5))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Count")
plt.show()
plt.figure(figsize=(8, 5))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
