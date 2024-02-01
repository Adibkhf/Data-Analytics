import pandas as pd

# Load the dataset
df = pd.read_csv('Iowa_Liquor_Sales.csv')

# Handle mixed data types
# Example: Converting Zip Code to string
df['Zip Code'] = df['Zip Code'].astype(str)

# Handle missing values
# Example: Fill missing values or drop rows/columns
df['County Number'].fillna(value=df['County Number'].mode()[0], inplace=True)


# Drop unnecessary columns
df.drop(columns=['Invoice/Item Number'], inplace=True)
df = df.drop(['Vendor Number', 'Item Number', 'Item Description'], axis=1)

# Remove rows with missing values (NAs)
df.dropna(inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

# Convert data types
# Converting 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Converting 'State Bottle Cost', 'State Bottle Retail', and 'Sale (Dollars)' to numeric
df['State Bottle Cost'] = pd.to_numeric(df['State Bottle Cost'].str.replace('$', ''))
df['State Bottle Retail'] = pd.to_numeric(df['State Bottle Retail'].str.replace('$', ''))
df['Sale (Dollars)'] = pd.to_numeric(df['Sale (Dollars)'].str.replace('$', ''))

# Ensure consistent formatting for geographical data
df['City'] = df['City'].str.title()  # Capitalize city names
df['County'] = df['County'].str.title()  # Capitalize county names

# Extracting month and day of the week from the 'Date' column
df['Month'] = df['Date'].dt.month
df['DayOfWeek'] = df['Date'].dt.dayofweek

# Save the cleaned dataset
df.to_csv('Iowa_Liquor_Sales_Cleaned.csv', index=False)
