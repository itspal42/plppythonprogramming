import pandas as pd

# Load the dataset (from a CSV file, for example)
# If you're using a local file, replace the URL with the file path
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
df = pd.read_csv(url, header=None, names=columns)

# Display the first few rows of the dataset
print(df.head())
# Check the data types of each column
print(df.dtypes)

# Check for missing values
print(df.isnull().sum())
# Option 1: Fill missing values with the column mean (if there were any missing values)
# df.fillna(df.mean(), inplace=True)

# Option 2: Drop rows with missing values
df.dropna(inplace=True)

# Verify that no more missing values exist
print(df.isnull().sum())
# Check the cleaned data (no missing values now)
print(df.head())
