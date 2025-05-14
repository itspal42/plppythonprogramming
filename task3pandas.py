import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the Iris dataset from a URL (replace with the path if using a local file)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv(url, header=None, names=columns)

# Display the first few rows of the dataset
print(df.head())

# Let's assume we want to plot sepal length over an arbitrary "time" (by species in sorted order)
df_sorted = df.sort_values('sepal_length')

plt.figure(figsize=(10, 6))
sns.lineplot(x=df_sorted.index, y=df_sorted['sepal_length'], hue=df_sorted['species'])
plt.title('Trends in Sepal Length Over Data Points')
plt.xlabel('Index (simulating time)')
plt.ylabel('Sepal Length (cm)')
plt.legend(title='Species')
plt.show()

# Bar chart for average petal length per species
plt.figure(figsize=(10, 6))
sns.barplot(x='species', y='petal_length', data=df)
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# Scatter plot for sepal length vs petal length
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='petal_length', hue='species', data=df, palette='Set1')
plt.title('Relationship Between Sepal Length and Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')
plt.show()
