# Iowa Alcohol Sales Data Analysis

## Overview

This project delves into the Iowa Alcohol Sales dataset, encompassing detailed transaction records from Iowan liquor stores. The dataset offers a rich array of data fields including transaction identifiers, dates, store details (number, name, address, location), category information, vendor details, and specifics of the liquor sold (type, volume, cost, sales figures). Our analysis aims to unearth key insights into consumer purchasing patterns, popular liquor categories, sales trends, and geographical distribution of alcohol sales in Iowa. 

## Dataset Source

The dataset for this analysis has been sourced from Kaggle. It can be accessed and downloaded from the following link: [Iowa Liquor Sales Dataset on Kaggle](https://www.kaggle.com/datasets/residentmario/iowa-liquor-sales?resource=download).

## Objectives

Our primary objectives are to:

- Clean and preprocess the dataset for robust analysis.
- Perform exploratory data analysis to uncover underlying patterns.
- Visualize the data to reveal trends and insights.
- Provide answers to critical questions relating to alcohol sales.

## Potential Analysis Questions

1. What are the top-selling liquor categories in Iowa?
2. How do liquor sales vary by region and store location?
3. What are the peak sales periods for liquor in Iowa?
4. Is there a correlation between the type of liquor sold and the location of the store?
5. What are the pricing trends for different types of liquor?
6. Are there any notable differences in sales patterns between counties?
7. What is the distribution of alcohol sales across different store sizes?
8. How does legislative change or population growth affect the volume of alcohol sold in gallons over the years?
9. Is there a correlation between the type of liquor sold and the location of the store?
10. What are the trends in liquor sales volume (in liters and gallons) over time in Iowa?

## Dataset Description

The dataset includes the following columns:

- Invoice/Item Number
- Date
- Store Number
- Store Name
- Address
- City
- Zip Code
- Store Location
- County Number
- County
- Category
- Category Name
- Vendor Number
- Vendor Name
- Item Number
- Item Description
- Pack
- Bottle Volume (ml)
- State Bottle Cost
- State Bottle Retail
- Bottles Sold
- Sale (Dollars)
- Volume Sold (Liters)
- Volume Sold (Gallons)

## Data Analysis Workflow

1. [**Data Discovery**](./Data%20Discovery.py) - Initial exploration of the raw dataset to understand its structure, check for missing values, and determine data types.
2. [**Data Cleaning**](./Data%20Cleaning.py) - Cleaning the dataset to handle missing values, fix data type inconsistencies, and remove duplicates to ensure the integrity of the data.
3. [**Data Transformation**](./Data%20Transformation.py) - Manipulating the dataset through sorting, aggregating, and other transformations to format the data for analysis.
4. [**Exploratory Data Analysis (EDA)**](./Iowa_Liquor_Sales_Analysis.ipynb) - Conducting EDA to discover patterns, detect anomalies, and generate hypotheses from the dataset, with visualizations to support findings.
5. [**SQL Data Exploration**](./EDA.sql) - Utilizing SQL queries for in-depth analysis and to extract specific insights from the dataset.
6. [**Pandas Data Analysis**](./EDA%20Pandas.py) - Leveraging the Pandas library in Python for data analysis to complement SQL findings.
7. [**BigQuery Data Analysis**](./EDA_BigQuery.py) - Performing advanced data analysis using Google BigQuery to handle large-scale data efficiently and extract complex insights.

## Methodology

- **Python Libraries:** Utilization of Pandas, NumPy, and Matplotlib for data manipulation and visualization.
- **Data Cleaning and Transformation:** Ensuring data quality and appropriateness for analysis.
- **EDA and Visualization:** Employing statistical techniques and visualization tools to extract and present insights.

## Download Transformed Dataset

The transformed dataset, ready for analysis, is available for download. You can access it via the following link: [Download Transformed Dataset](https://drive.google.com/file/d/1tPRLodYTXV8fO2tyQgsjc-VEKX_xhdeA/view?usp=sharing).

## Summary 
