import pandas as pd

# Assuming your data is in a CSV file for Pandas to read
df = pd.read_excel('Car data (clean).xlsx')


# Average price of cars by make
avg_price_by_make = df.groupby('Make')['Price'].mean()

# Count of cars by city and make
count_by_city_make = df.groupby(['City', 'Make']).size().reset_index(name='Total Cars')

# Most common car type in each city
most_common_type_by_city = df.groupby(['City', 'Type']).size().reset_index(name='Count').sort_values(['City', 'Count'], ascending=[True, False])

# Average mileage of cars by year of first registration
avg_mileage_by_year = df.groupby('Year of First Registration')['Mileage'].mean()

# Highest priced car in each make
highest_price_by_make = df.groupby('Make')['Price'].max()

# List of cars with mileage greater than average mileage
avg_mileage = df['Mileage'].mean()
cars_above_avg_mileage = df[df['Mileage'] > avg_mileage]

# Average age of diesel and essence cars
avg_age_by_engine = df[df['Engine'].isin(['Diesel', 'Essence'])].groupby('Engine')['Car Age'].mean()

# Cars with price higher than the average price of their make
avg_price_by_make = df.groupby('Make')['Price'].transform('mean')
cars_above_avg_price = df[df['Price'] > avg_price_by_make]

# Number of cars per fiscal power category
cars_by_fiscal_power = df.groupby('Fiscal Power').size().reset_index(name='Number of Cars')

# List of cars from a specific source with price below a certain threshold
cars_from_source_below_price = df[(df['Source'] == 'Moteur.ma') & (df['Price'] < 100000)]

# Finding cars priced above the average for their specific type and city
avg_price_by_city_type = df.groupby(['City', 'Type'])['Price'].transform('mean')
cars_above_avg_city_type = df[df['Price'] > avg_price_by_city_type]

# Calculating the average annual depreciation rate of car prices by make and year
depreciation_rate = df.groupby(['Make', 'Year of First Registration']).agg(yearly_depreciation_rate=pd.NamedAgg(column='Price', aggfunc=lambda x: (x.max() - x.min()) / len(x.unique())))

# Identifying the top 5 most popular car makes in each city based on the number of listings
top_5_makes_in_city = df.groupby(['City', 'Make']).size().reset_index(name='Total Cars').sort_values(['City', 'Total Cars'], ascending=[True, False]).groupby('City').head(5)

# Analyzing how prices vary with different engine types and fiscal power ratings
price_stats_by_engine_fiscal = df.groupby(['Engine', 'Fiscal Power'])['Price'].agg(['mean', 'min', 'max']).rename(columns={'mean': 'Average Price', 'min': 'Min Price', 'max': 'Max Price'})

# Finding cars whose mileage is significantly higher than the average for their make and year
avg_mileage_by_make_year = df.groupby(['Make', 'Year of First Registration'])['Mileage'].transform('mean') * 1.5
cars_with_high_mileage = df[df['Mileage'] > avg_mileage_by_make_year]
    
# Investigating how price correlates with car age and mileage
price_correlation = df.groupby(['Car Age', 'Mileage'])['Price'].mean().reset_index(name='Average Price')

# Providing a frequency distribution of different car types
type_frequency = df.groupby('Type').size().reset_index(name='Frequency')

# Focusing on the average price of cars by city and make for cars registered in the last 5 years
recent_cars_avg_price = df[df['Year of First Registration'] >= df['Year of First Registration'].max() - 5].groupby(['City', 'Make'])['Price'].mean().reset_index(name='Average Price')

# Selecting cars priced in the top 10% within their respective make
top_10_percent_price_by_make = df.groupby('Make')['Price'].transform(lambda x: x.quantile(0.9))
cars_in_top_10_percent = df[df['Price'] >= top_10_percent_price_by_make]

# Examining the relationship between fiscal power, engine type, and car price
relationship_fiscal_engine_price = df.groupby(['Fiscal Power', 'Engine'])['Price'].agg(['mean', 'min', 'max']).rename(columns={'mean': 'Average Price', 'min': 'Min Price', 'max': 'Max Price'})
