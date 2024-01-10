-- SQL Script for Car Prices Analysis

-- 1. Creation of the table
CREATE TABLE car_market_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    price INT,
    type VARCHAR(50),
    year_of_first_registration INT,
    engine VARCHAR(50),
    fiscal_power INT,
    mileage INT,
    source VARCHAR(50),
    car_age INT,
    make VARCHAR(50),
    model VARCHAR(50)
);

-- 2. Ingest data from an external file
-- This step is typically done through a MySQL client or command line tool.
-- For example, using MySQL Workbench or a command like:
-- LOAD DATA INFILE 'path_to_your_csv_file.csv' 
-- INTO TABLE car_market_data
-- FIELDS TERMINATED BY ',' ENCLOSED BY '"'
-- LINES TERMINATED BY '\n'
-- IGNORE 1 ROWS;

-- 3. Example Queries

-- Average price of cars by make
SELECT make, AVG(price) AS average_price
FROM car_market_data
GROUP BY make;

-- Count of cars by city and make
SELECT city, make, COUNT(*) as total_cars
FROM car_market_data
GROUP BY city, make;

-- Most common car type in each city
SELECT city, type, COUNT(*) as count
FROM car_market_data
GROUP BY city, type
ORDER BY city, count DESC;

-- Average mileage of cars by year of first registration
SELECT year_of_first_registration, AVG(mileage) as average_mileage
FROM car_market_data
GROUP BY year_of_first_registration;

-- Highest priced car in each make
SELECT make, MAX(price) as highest_price
FROM car_market_data
GROUP BY make;

-- List of cars with mileage greater than average mileage
SELECT * 
FROM car_market_data
WHERE mileage > (SELECT AVG(mileage) FROM car_market_data);

-- Average age of diesel and essence cars
SELECT engine, AVG(car_age) as average_age
FROM car_market_data
WHERE engine IN ('Diesel', 'Essence')
GROUP BY engine;

-- Cars with price higher than the average price of their make
SELECT *
FROM car_market_data
WHERE price > (
    SELECT AVG(price)
    FROM car_market_data AS subquery
    WHERE subquery.make = car_market_data.make
);

-- Number of cars per fiscal power category
SELECT fiscal_power, COUNT(*) as number_of_cars
FROM car_market_data
GROUP BY fiscal_power;

-- List of cars from a specific source with price below a certain threshold
SELECT *
FROM car_market_data
WHERE source = 'Moteur.ma' AND price < 100000;

-- Finding cars priced above the average for their specific type and city.
SELECT *
FROM car_market_data
WHERE (city, type, price) IN (
    SELECT city, type, AVG(price) as avg_price
    FROM car_market_data
    GROUP BY city, type
    HAVING price > avg_price
);

-- Calculates the average annual depreciation rate of car prices by make and year.
SELECT make, year_of_first_registration, 
       (MAX(price) - MIN(price)) / COUNT(DISTINCT year_of_first_registration) AS yearly_depreciation_rate
FROM car_market_data
GROUP BY make, year_of_first_registration;

-- Identifies the top 5 most popular car makes in each city based on the number of listings.
SELECT city, make, COUNT(*) as total_cars
FROM car_market_data
GROUP BY city, make
ORDER BY city, total_cars DESC
LIMIT 5;

-- Analyzes how prices vary with different engine types and fiscal power ratings.
SELECT engine, fiscal_power, AVG(price) as average_price, MIN(price) as min_price, MAX(price) as max_price
FROM car_market_data
GROUP BY engine, fiscal_power;

-- Finds cars whose mileage is significantly higher than the average for their make and year.
SELECT *
FROM car_market_data
WHERE (make, year_of_first_registration, mileage) IN (
    SELECT make, year_of_first_registration, AVG(mileage) * 1.5 as high_mileage
    FROM car_market_data
    GROUP BY make, year_of_first_registration
    HAVING mileage > high_mileage
);

-- Investigates how price correlates with car age and mileage.
SELECT car_age, mileage, AVG(price) as average_price
FROM car_market_data
GROUP BY car_age, mileage;

-- Provides a frequency distribution of different car types.
SELECT type, COUNT(*) as frequency
FROM car_market_data
GROUP BY type;

-- Focuses on the average price of cars by city and make for cars registered in the last 5 years.
SELECT city, make, AVG(price) as average_price
FROM car_market_data
WHERE year_of_first_registration >= YEAR(CURDATE()) - 5
GROUP BY city, make;

-- Selects cars priced in the top 10% within their respective make.
SELECT a.*
FROM car_market_data a
JOIN (
    SELECT make, PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY price) as top_10_percent_price
    FROM car_market_data
    GROUP BY make
) b ON a.make = b.make
WHERE a.price >= b.top_10_percent_price;

-- Examines the relationship between fiscal power, engine type, and car price.
SELECT fiscal_power, engine, AVG(price) as average_price, MIN(price) as min_price, MAX(price) as max_price
FROM car_market_data
GROUP BY fiscal_power, engine;

