import pandas as pd 

# Load the dataset
df = pd.read_csv('Iowa_Liquor_Sales.csv')

# Display basic information about the dataset
print("--------------------------------------------------------------------------------")
print("Overview of the raw data:")
print("--------------------------------------------------------------------------------")
print(df.info())
print("\n")

# Display the first few rows of the dataset
print(df.head())
print("--------------------------------------------------------------------------------")


# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())
print("--------------------------------------------------------------------------------")

# Check data types
print("Data Types:")
print(df.dtypes)
print("--------------------------------------------------------------------------------")

# Count of unique values in each column
print("Count of unique values in each column:")
print(df.nunique())
print("--------------------------------------------------------------------------------")

# Summary statistics for numerical columns
print("Summary statistics for numerical columns:")
print(df.describe())
print("--------------------------------------------------------------------------------")

# Description of non-numeric columns to understand categorical data
print("Description of non-numeric columns:")
print(df.describe(include=['object']))
print("--------------------------------------------------------------------------------")

# Memory usage by column to understand dataset size and efficiency
print("Memory usage by column:")
print(df.memory_usage(deep=True))
print("--------------------------------------------------------------------------------")

# Sample of Random Rows
print("Random sample of rows:")
print(df.sample(5))
