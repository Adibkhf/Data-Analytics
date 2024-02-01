import pandas as pd
import re 

# Load the cleaned dataset
df = pd.read_csv('Iowa_Liquor_Sales_Cleaned.csv')



# Time-Related Features
df['Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.weekday

# Profit and Sales Metrics
df['Profit per Bottle'] = df['State Bottle Retail'] - df['State Bottle Cost']
df['Total Profit'] = df['Profit per Bottle'] * df['Bottles Sold']
df['Sales per Liter'] = df['Sale (Dollars)'] / df['Volume Sold (Liters)']


# Removing Outliers

# Function to remove outliers based on IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Apply the function to columns where outliers are likely to be present
df = remove_outliers(df, 'Total Profit')
df = remove_outliers(df, 'Sales per Liter')
df = remove_outliers(df, 'Bottles Sold')


# Regional Metrics
# (Assuming the existence of region or county information)
df['Total Sales by County'] = df.groupby('County')['Sale (Dollars)'].transform('sum')
df['Total Sales by Store Location'] = df.groupby('Store Location')['Sale (Dollars)'].transform('sum')


# Vendor Contribution
df['Total Sales by Vendor'] = df.groupby('Vendor Name')['Sale (Dollars)'].transform('sum')

#Extract Longitude and Latitude
def extract_lat_long(text):
    match = re.search(r"\(([^)]+)", text)
    if match:
        coords = match.group(1).split(',')
        if len(coords) == 2:
            return float(coords[0].strip()), float(coords[1].strip())
    return None, None

# Apply the function to the 'Store Location' column
df['Latitude'], df['Longitude'] = zip(*df['Store Location'].apply(extract_lat_long))


df = df.dropna(subset=['Latitude', 'Longitude'])

# Save the transformed dataset
df.to_csv('Iowa_Liquor_Sales_Transformed.csv', index=False)
