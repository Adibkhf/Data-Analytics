import pandas as pd 
import numpy as np

#moteur.ma dataset
df_moteur_ma = pd.read_excel('data_moteur_ma.xlsx')

#tomobila.ma dataset
df_link_tomobila_ma = pd.read_excel('Link tomobila_ma.xlsx')

df_tomobila_ma = pd.read_excel('data_tomobila_ma.xlsx') 

# Function to clean and standardize 'Type' column
def clean_type(type_str):
    if pd.isnull(type_str):
        return type_str
    words = type_str.strip().split()[:2]  # Take only the first two words
    return ' '.join(words).lower()  # Join the words with a space and convert to lower case

# Function to extract 'Ville' from 'Type'
def extract_ville(type_str):
    if pd.isnull(type_str):
        return type_str
    return type_str.strip().split()[-1].lower()

# Function to clean 'Kilométrage' column
def clean_kilometrage(km):
    if pd.isnull(km):
        return km
    # Keep only digits and convert to integer
    km_numeric = ''.join(filter(str.isdigit, km))
    return km_numeric if km_numeric else None

# Clean 'Type' and 'Kilométrage' in both DataFrames
df_link_tomobila_ma['Ville'] = df_link_tomobila_ma['Type'].apply(extract_ville)
df_link_tomobila_ma['Type'] = df_link_tomobila_ma['Type'].apply(clean_type)
df_link_tomobila_ma['Kilométrage'] = df_link_tomobila_ma['Kilométrage'].apply(clean_kilometrage)

df_tomobila_ma['Type'] = df_tomobila_ma['Type'].apply(clean_type)
df_tomobila_ma['Kilométrage'] = df_tomobila_ma['Kilométrage'].apply(clean_kilometrage)
df_tomobila_ma['Ville'] = [x.lower() if isinstance(x, str) else x for x in df_tomobila_ma['Ville']]

# Now we can proceed with the merge
merged_df = pd.merge(df_tomobila_ma, df_link_tomobila_ma, on=['Type', 'Kilométrage','Ville'], how='left', suffixes=('', '_link'))

# Fill missing 'Price' values in df_tomobila_ma with 'Price' values from df_link_tomobila_ma
merged_df['Price'] = merged_df['Price'].fillna(merged_df['Price_link'])

# Drop the extra 'Price' column from df_link_tomobila_ma
merged_df.drop('Price_link', axis=1, inplace=True)

merged_df = merged_df.drop_duplicates()

#The final dataset with the price included 
df_tomobila_ma = merged_df.drop_duplicates(subset=['Type', 'Kilométrage', 'Ville'])


#wandaloo.ma dataset 
df_wandaloo_ma = pd.read_excel('data_wandaloo_ma.xlsx')


# Rename columns to English
df_moteur_ma.rename(columns={
    'Année': 'Year of First Registration',
    'Boite de vitesses': 'Transmission',
    'Date': 'Date Posted',
    'Puissance fiscale': 'Fiscal Power',
    'Nombre de portes': 'Doors',
    'Couleur': 'Color',
    'Body Type': 'Body Type',
    'Véhicule dédouané': 'Customs Cleared',
    'Première main': 'First Hand',
    'Véhicule en garantie': 'Under Warranty',
    'Voiture personnalisée (tuning)': 'Customized Car',
    'Importé neuf': 'Imported New',
    'Véhicule neuf': 'New Vehicle',
    'Fuel':'Engine',
    'Kilométrage': 'Mileage',
    'Carburant':'Engine'
}, inplace=True)

df_tomobila_ma.rename(columns={
    'Mise en Circulation': 'Year of First Registration',
    'Marque': 'Brand',
    'Modéle': 'Model',
    'Ville': 'City',
    'Origine': 'Origin',
    'Kilométrage': 'Mileage',
    'Etat': 'Condition',
    'Dédouanement': 'Customs Clearance',
    'Date Dédouanement': 'Customs Clearance Date',
    'Transmission': 'Transmission',
    'Climatisation': 'Air Conditioning',
    'Couleur Externe': 'Exterior Color',
    'Portes': 'Doors',
    'Propriétaires': 'Owners',
    'Carrosserie': 'Body Type',
    'Carburant': 'Engine',
    'Consommation': 'Consumption',
    'Puissance Fiscale': 'Fiscal Power',
    'Garantie': 'Warranty',
}, inplace=True)




# Renaming for df_wandaloo_ma
df_wandaloo_ma.rename(columns={
    'Modèle': 'Model',
    'Ville': 'City',
    'Vendeur': 'Seller',
    'Main': 'Hand',
    'Kilométrage': 'Mileage',
    'Carburant': 'Fuel',
    'Transmision': 'Transmission',
    'Année de mise en circulation': 'Year of First Registration',
    'Motorisation': 'Engine',
    'Puissance fiscale': 'Fiscal Power',
    'Puissance dynamique': 'Dynamic Power'
}, inplace=True)

# Select common columns (translated)
common_columns = ['City','Price','Type', 'Year of First Registration', 
                  'Engine', 'Fiscal Power','Mileage','Source']


df_wandaloo_ma['Source'] = ['Wandaloo.ma' for x in df_wandaloo_ma['Price']]

df_tomobila_ma['Source'] = ['Tomobila.ma' for x in df_tomobila_ma['Price']]

df_moteur_ma['Source'] = ['Moteur.ma' for x in df_moteur_ma['Price']]


df_moteur_ma = df_moteur_ma[common_columns]
df_tomobila_ma = df_tomobila_ma[common_columns]
df_wandaloo_ma = df_wandaloo_ma[common_columns]

df_combined = pd.concat([
    df_moteur_ma[common_columns],
    df_tomobila_ma[common_columns],
    df_wandaloo_ma[common_columns]
], ignore_index=True)


df_combined.to_excel('data_Morocco_cars.xlsx')
