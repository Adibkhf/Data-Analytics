# Car Prices Analysis of the Moroccan Market

## Project Overview
This project is dedicated to exploring and understanding the dynamics of the Moroccan car market. Comprehensive data from major car listing websites - moteur.ma, tomobila.ma, and wandaloo.ma - has been meticulously collected and analyzed to provide deep insights into the market.
![Car Analysis](car.png)

### Data Collection
The data collection process involved two stages for each source:
1. **Link Extraction**: Scripts were developed to identify relevant car listing links.
2. **Data Extraction**: Essential information was extracted from each listing.

Using `data_concatenation.py`, these datasets were merged into one, standardizing column names and ensuring consistency.

### Dataset
The final dataset consists of columns: 'Price', 'Type', 'Year of First Registration', 'Engine', 'Fiscal Power', 'City', 'Mileage', and 'Source'. It provides insights into pricing strategies, model preferences, and technical specifications' impact on car value.

## Analysis Objectives
The project aims to answer critical questions about the Moroccan car market:

1. **Key Factors Influencing Car Prices**: Identifying variables that significantly impact car pricing.
2. **Car Value Depreciation Over Time**: Analyzing how the age of a car affects its market value.
3. **Regional Preferences for Car Models and Types**: Exploring variations in preferences across different regions.
4. **Relationship Between Mileage and Car Prices**: Understanding how usage impacts a car's value.
5. **Impact of Engine Specifications on Prices and Popularity**: Analyzing consumer preferences regarding performance and efficiency.

## Tools and Technologies Used
- **Python**: For data cleaning, manipulation, and exploratory data analysis.
- **SQL**: For database management and queries.
- **Tableau**: For creating an Interactive Dashboard to visualize findings.

## Repository Structure
- [`Car data (clean).xlsx`](./Car%20data%20(clean).xlsx): Cleaned dataset.
- [`Car prices Analysis.ipynb`](./Car%20prices%20Analysis.ipynb): Jupyter notebook for analysis.
- [`car.png`](./car.png), [`car2.png`](./car2.png): Project-related images.
- [`data_concatenation.py`](./data_concatenation.py): Script for merging datasets.
- [`data_Morocco_cars.xlsx`](./data_Morocco_cars.xlsx), [`data_moteur_ma.xlsx`](./data_moteur_ma.xlsx), [`data_tomobila_ma.xlsx`](./data_tomobila_ma.xlsx), [`data_wandaloo_ma.xlsx`](./data_wandaloo_ma.xlsx): Raw datasets.
- [`Extract_link_moteur_ma.py`](./Extract_link_moteur_ma.py), [`Extract_link_tomobila_ma.py`](./Extract_link_tomobila_ma.py), [`extract_link_wandaloo.py`](./extract_link_wandaloo.py): Scripts for extracting links.
- [`Liens voitures.xlsx`](./Liens%20voitures.xlsx), [`Link moteur_ma.xlsx`](./Link%20moteur_ma.xlsx), [`Link tomobila_ma.xlsx`](./Link%20tomobila_ma.xlsx), [`Link wandaloo.xlsx`](./Link%20wandaloo.xlsx): Extracted links.
- [`scrap_moteur_ma.py`](./scrap_moteur_ma.py), [`scrap_tomobila_ma.py`](./scrap_tomobila_ma.py), [`scrap_wandaloo.py`](./scrap_wandaloo.py): Web scraping scripts.
- [`EDA Analysis.sql`](./EDA%20Analysis.sql): SQL queries for data analysis.
- [`EDA Analysis pandas.py`](./EDA%20Analysis%20pandas.py): Pandas file equivalent of SQL queries.
## Dashboard
- Tableau Online
- [!(Car visualization.PNG)](https://public.tableau.com/app/profile/adib.khaffaji/viz/Tableau_viz_of_car_price_analysis/Dashboard1)


