from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

# Calculate total sales for each category per year.
query_total_sales_per_category_year = """
SELECT 
  EXTRACT(YEAR FROM Date) AS Year,
  Category_Name,
  SUM(Sale_Dollars) AS TotalSales
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`
GROUP BY 
  Year, Category_Name
ORDER BY 
  Year, TotalSales DESC;
"""

# Identify top-selling stores in terms of volume sold.
query_top_selling_stores = """
SELECT 
  Store_Number,
  Store_Name,
  SUM(Volume_Sold__Liters_) AS TotalVolumeSold
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`
GROUP BY 
  Store_Number, Store_Name
ORDER BY 
  TotalVolumeSold DESC
LIMIT 10;
"""

# Determine the average sale amount per transaction.
query_avg_sale_per_transaction = """
SELECT 
  AVG(Sale_Dollars) AS AvgSaleAmount
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`;
"""

# Find the correlation between pack size and total sales.
query_pack_size_correlation = """
SELECT 
  CORR(Pack, Sale_Dollars) AS CorrelationCoefficient
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`;
"""

# Calculate monthly sales trends for the most recent year in the dataset.
query_monthly_sales_trends = """
SELECT 
  EXTRACT(MONTH FROM Date) AS Month,
  SUM(Sale_Dollars) AS TotalSales
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`
WHERE 
  EXTRACT(YEAR FROM Date) = (SELECT MAX(EXTRACT(YEAR FROM Date)) FROM `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`)
GROUP BY 
  Month
ORDER BY 
  Month;
"""

# Analyze the day of the week with the highest average sales.
query_sales_by_weekday = """
SELECT 
  DayOfWeek AS Weekday,
  AVG(Sale_Dollars) AS AvgSales
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`
GROUP BY 
  DayOfWeek
ORDER BY 
  AvgSales DESC;
"""

# Identify the county with the highest number of unique liquor categories sold.
query_county_unique_liquor_categories = """
SELECT 
  County,
  COUNT(DISTINCT Category) AS UniqueCategoriesCount
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`
GROUP BY 
  County
ORDER BY 
  UniqueCategoriesCount DESC
LIMIT 1;
"""

# Determine sales performance by comparing the first and second half of the year.
query_sales_performance_h1_vs_h2 = """
SELECT 
  IF(EXTRACT(MONTH FROM Date) <= 6, 'H1', 'H2') AS HalfOfYear,
  SUM(Sale_Dollars) AS TotalSales
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`
GROUP BY 
  HalfOfYear;
"""

# Find the percentage share of each category in total sales.
query_category_share_of_total_sales = """
SELECT 
  Category_Name,
  SUM(Sale_Dollars) AS CategorySales,
  SUM(Sale_Dollars) / (SELECT SUM(Sale_Dollars) FROM `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`) AS PercentageOfTotalSales
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`
GROUP BY 
  Category_Name
ORDER BY 
  CategorySales DESC;
"""

# Examine the impact of bottle volume on the number of bottles sold.
query_impact_of_bottle_volume_on_sales = """
SELECT 
  Bottle_Volume_ml,
  SUM(Bottles_Sold) AS TotalBottlesSold,
  AVG(Bottles_Sold) AS AvgBottlesSold
FROM 
  `omega-tenure-413015.IOWA_LIQUOR_ANALYSIS.transformed`
GROUP BY 
  Bottle_Volume_ml
ORDER BY 
  TotalBottlesSold DESC;
"""

# Dictionary of queries
query_dict = {
    'total_sales_per_category_year': query_total_sales_per_category_year,
    'top_selling_stores': query_top_selling_stores,
    'avg_sale_per_transaction': query_avg_sale_per_transaction,
    'pack_size_correlation': query_pack_size_correlation,
    'monthly_sales_trends': query_monthly_sales_trends,
    'sales_by_weekday': query_sales_by_weekday,
    'county_unique_liquor_categories': query_county_unique_liquor_categories,
    'sales_performance_h1_vs_h2': query_sales_performance_h1_vs_h2,
    'category_share_of_total_sales': query_category_share_of_total_sales,
    'impact_of_bottle_volume_on_sales': query_impact_of_bottle_volume_on_sales
}

# Function to execute each query
def execute_query(query):
    query_job = client.query(query)  # Make an API request.
    return query_job.result()  # Wait for the job to complete.

# Execute and print results of all queries
for name, query in query_dict.items():
    print(f"Executing {name}...")
    for row in execute_query(query):
        print(row)
