# Importing pandas
import pandas as pd

# Assuming your dataframe is named 'df'
df = pd.read_csv('Iowa_Liquor_Sales_Transformed.csv')


# 1. Yearly growth rate in total sales
yearly_growth_rate = df.groupby('Year')['Sale (Dollars)'].sum().pct_change()

# 2. Average monthly sales per store
avg_monthly_sales_per_store = df.groupby(['Store Number', 'Month'])['Sale (Dollars)'].mean()

# 3. Top 5 categories with the highest average profit
top5_categories_by_avg_profit = df.groupby('Category')['Profit per Bottle'].mean().nlargest(5)

# 4. Store with the most diverse range of categories
store_with_most_categories = df.groupby('Store Number')['Category'].nunique().idxmax()

# 5. Month with the highest average sale volume (Liters) per transaction
month_highest_avg_volume = df.groupby('Month')['Volume Sold (Liters)'].mean().idxmax()

# 6. Correlation between bottle volume and total sales
corr_bottle_volume_sales = df[['Bottle Volume (ml)', 'Sale (Dollars)']].corr().iloc[0,1]

# 7. Most profitable day of the week
most_profitable_weekday = df.groupby('Weekday')['Total Profit'].mean().idxmax()

# 8. Sales trend over the years (using linear regression)
from scipy.stats import linregress
sales_trend = linregress(df['Year'], df['Sale (Dollars)'])

# 9. Average sale per transaction for each category
avg_sale_per_transaction_category = df.groupby('Category')['Sale (Dollars)'].mean()

# 10. Store with the highest ratio of profit to total sales
profit_to_sales_ratio = (df.groupby('Store Number')['Total Profit'].sum() / df.groupby('Store Number')['Sale (Dollars)'].sum()).idxmax()

# 11. Top 3 counties by average sales per liter
top3_counties_avg_sales_per_liter = df.groupby('County')['Sales per Liter'].mean().nlargest(3)

# 12. Seasonal analysis of sales (assuming 1:Winter, 2:Spring, 3:Summer, 4:Fall)
df['Season'] = df['Month'].apply(lambda x: (x%12 + 3)//3)
seasonal_sales_analysis = df.groupby('Season')['Sale (Dollars)'].sum()

# 13. Store with the highest year-over-year growth
year_over_year_growth = df.pivot_table(values='Sale (Dollars)', index='Store Number', columns='Year', aggfunc='sum').pct_change(axis=1).max(axis=1).idxmax()

# 14. Average profit margin per transaction
avg_profit_margin = (df['Total Profit'] / df['Sale (Dollars)']).mean()

# 15. Day of month with highest average sales
day_of_month_highest_sales = df.groupby('Day')['Sale (Dollars)'].mean().idxmax()

# 16. Effect of pack size on average sales
effect_pack_size = df.groupby('Pack')['Sale (Dollars)'].mean()

# 17. Comparison of average sales per liter between counties
avg_sales_per_liter_comparison = df.groupby('County')['Sales per Liter'].mean()

# 18. Store location with the highest average bottle profit
highest_avg_bottle_profit_location = df.groupby('Store Location')['Profit per Bottle'].mean().idxmax()

# 19. Yearly distribution of number of transactions
yearly_transactions_distribution = df.groupby('Year').size()

# 20. Average sales per transaction by vendor
avg_sales_per_transaction_by_vendor = df.groupby('Vendor Name')['Sale (Dollars)'].mean()
