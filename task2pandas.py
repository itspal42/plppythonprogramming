import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Iris dataset from a URL (replace with the path if using a local file)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv(url, header=None, names=columns)

# Display the first few rows of the dataset
print(df.head())

# Compute basic statistics of the numerical columns
statistics = df.describe()
print(statistics)

# Group by species and compute the mean of numerical columns
grouped = df.groupby('species').mean()
print(grouped)


# Boxplot for sepal length by species
sns.boxplot(x='species', y='sepal_length', data=df)
plt.title('Sepal Length by Species')
plt.show()

# Scatterplot between petal length and petal width
sns.scatterplot(x='petal_length', y='petal_width', hue='species', data=df)
plt.title('Petal Length vs Petal Width by Species')
plt.show()
