CREATE TABLE liquor_sales (
    Date DATE,
    StoreNumber INT,
    StoreName VARCHAR(255),
    Address VARCHAR(255),
    City VARCHAR(100),
    ZipCode VARCHAR(10),
    StoreLocation TEXT,
    CountyNumber INT,
    County VARCHAR(100),
    Category BIGINT,
    CategoryName VARCHAR(255),
    VendorName VARCHAR(255),
    Pack INT,
    BottleVolume_ml INT,
    StateBottleCost DECIMAL(10, 2),
    StateBottleRetail DECIMAL(10, 2),
    BottlesSold INT,
    SaleDollars DECIMAL(10, 2),
    VolumeSold_Liters DECIMAL(10, 2),
    VolumeSold_Gallons DECIMAL(10, 2),
    Month INT,
    DayOfWeek INT,
    Latitude DECIMAL(10, 7),
    Longitude DECIMAL(10, 7),
    Year INT,
    Day INT,
    Weekday INT,
    ProfitPerBottle DECIMAL(10, 2),
    TotalProfit DECIMAL(10, 2),
    SalesPerLiter DECIMAL(10, 2),
    TotalSalesByCounty DECIMAL(10, 2),
    TotalSalesByStoreLocation DECIMAL(10, 2),
    TotalSalesByVendor DECIMAL(10, 2)
);

-- Replace 'path/to/your/Iowa_Liquor_Sales_Transformed.csv' with the actual path to your CSV file
-- Also, the exact LOAD DATA syntax may vary depending on your SQL database system (MySQL, PostgreSQL, etc.)
LOAD DATA INFILE 'path/to/your/Iowa_Liquor_Sales_Transformed.csv'
INTO TABLE liquor_sales
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;


-- 1. Yearly growth rate in total sales
SELECT Year, SUM(SaleDollars) AS TotalSales,
    (SUM(SaleDollars) - LAG(SUM(SaleDollars)) OVER (ORDER BY Year)) / LAG(SUM(SaleDollars)) OVER (ORDER BY Year) AS GrowthRate
FROM liquor_sales
GROUP BY Year;

-- 2. Average monthly sales per store
SELECT StoreNumber, Month, AVG(SaleDollars) AS AvgMonthlySales
FROM liquor_sales
GROUP BY StoreNumber, Month;

-- 3. Top 5 categories with the highest average profit
SELECT Category, AVG(ProfitPerBottle) AS AvgProfit
FROM liquor_sales
GROUP BY Category
ORDER BY AvgProfit DESC
LIMIT 5;

-- 4. Store with the most diverse range of categories
SELECT StoreNumber, COUNT(DISTINCT Category) AS CategoryCount
FROM liquor_sales
GROUP BY StoreNumber
ORDER BY CategoryCount DESC
LIMIT 1;

-- 5. Month with the highest average sale volume (Liters) per transaction
SELECT Month, AVG(VolumeSold_Liters) AS AvgVolume
FROM liquor_sales
GROUP BY Month
ORDER BY AvgVolume DESC
LIMIT 1;

-- 6. Correlation between bottle volume and total sales
-- Note: SQL standard does not directly support correlation function; 

-- 7. Most profitable day of the week
SELECT Weekday, AVG(TotalProfit) AS AvgProfit
FROM liquor_sales
GROUP BY Weekday
ORDER BY AvgProfit DESC
LIMIT 1;

-- 8. Sales trend over the years (using linear regression)
-- Linear regression functions depend on the SQL database system; 

-- 9. Average sale per transaction for each category
SELECT Category, AVG(SaleDollars) AS AvgSalePerTransaction
FROM liquor_sales
GROUP BY Category;

-- 10. Store with the highest ratio of profit to total sales
SELECT StoreNumber, SUM(TotalProfit) / SUM(SaleDollars) AS ProfitToSalesRatio
FROM liquor_sales
GROUP BY StoreNumber
ORDER BY ProfitToSalesRatio DESC
LIMIT 1;

-- 11. Top 3 counties by average sales per liter
SELECT County, AVG(SalesPerLiter) AS AvgSalesPerLiter
FROM liquor_sales
GROUP BY County
ORDER BY AvgSalesPerLiter DESC
LIMIT 3;

-- 12. Seasonal analysis of sales (assuming 1:Winter, 2:Spring, 3:Summer, 4:Fall)
SELECT CASE 
         WHEN Month IN (12, 1, 2) THEN 'Winter'
         WHEN Month IN (3, 4, 5) THEN 'Spring'
         WHEN Month IN (6, 7, 8) THEN 'Summer'
         ELSE 'Fall'
       END AS Season,
       SUM(SaleDollars) AS TotalSales
FROM liquor_sales
GROUP BY Season;

-- 13. Store with the highest year-over-year growth
SELECT StoreNumber, 
       (SUM(CASE WHEN Year = (SELECT MAX(Year) FROM liquor_sales) THEN SaleDollars ELSE 0 END) -
        SUM(CASE WHEN Year = (SELECT MAX(Year) - 1 FROM liquor_sales) THEN SaleDollars ELSE 0 END)) / 
       SUM(CASE WHEN Year = (SELECT MAX(Year) - 1 FROM liquor_sales) THEN SaleDollars ELSE 0 END) AS YearOverYearGrowth
FROM liquor_sales
GROUP BY StoreNumber
ORDER BY YearOverYearGrowth DESC
LIMIT 1;

-- 14. Average profit margin per transaction
SELECT AVG(TotalProfit / SaleDollars) AS AvgProfitMargin
FROM liquor_sales
WHERE SaleDollars > 0;

-- 15. Day of month with highest average sales
SELECT Day, AVG(SaleDollars) AS AvgSales
FROM liquor_sales
GROUP BY Day
ORDER BY AvgSales DESC
LIMIT 1;

-- 16. Effect of pack size on average sales
SELECT Pack, AVG(SaleDollars) AS AvgSales
FROM liquor_sales
GROUP BY Pack;

-- 17. Comparison of average sales per liter between counties
SELECT County, AVG(SalesPerLiter) AS AvgSalesPerLiter
FROM liquor_sales
GROUP BY County;

-- 18. Store location with the highest average bottle profit
SELECT StoreLocation, AVG(ProfitPerBottle) AS AvgProfitPerBottle
FROM liquor_sales
GROUP BY StoreLocation
ORDER BY AvgProfitPerBottle DESC
LIMIT 1;

-- 19. Yearly distribution of number of transactions
SELECT Year, COUNT(*) AS NumberOfTransactions
FROM liquor_sales
GROUP BY Year;

-- 20. Average sales per transaction by vendor
SELECT VendorName, AVG(SaleDollars) AS AvgSalesPerTransaction
FROM liquor_sales
GROUP BY VendorName;
