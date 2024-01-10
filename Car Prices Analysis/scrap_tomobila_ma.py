from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        return None

def extract_data(soup):
    data_dict = {}
    try:
        Typee = soup.find('div',attrs = {'class':'title'}).find('a').get_text()
    except:
        Typee = ''
    try:
        Price = soup.find('div',attrs = {'class':'price'}).find('span',attrs = {'class':'heading-font'}).get_text()
    except:
        Price = ''
    data_dict['Type'] = Typee
    data_dict['Price'] = Price
    # Iterate through all 'td' elements
    for td in soup.find_all('td'):
        # Find a nested table
        nested_table = td.find('table', class_='inner-table')
        if nested_table:
            # Find the key and value 'td' elements
            key_td = nested_table.find('td', class_='label-td')
            value_td = nested_table.find('td', class_='heading-font')
            if key_td and value_td:
                # Extract text and strip to clean it
                key = key_td.get_text(strip=True)
                value = value_td.get_text(strip=True)
                data_dict[key] = value
    return data_dict

def fetch_and_extract_data(url):
    soup = get_data(url)
    if soup:
        return extract_data(soup)
    else:
        return {}


# Load URLs from Excel file
df = pd.read_excel('Link tomobila_ma.xlsx')
links = df['Link'].tolist()

import logging

# Setup logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch_and_extract_data, link) for link in links]
    results = []
    for future in as_completed(futures):
        try:
            result = future.result()
            if result:
                results.append(result)
        except Exception as exc:
            logging.error(f'Error in thread: {exc}')

df_res = pd.DataFrame(results)
df_res.to_excel('data_tomobila_ma.xlsx')


