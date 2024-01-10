
from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
import requests
import pandas as pd

def setup_session():
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    })
    return session

session = setup_session()

def get_data(link):
    try:
        response = session.get(link, verify=False)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching {link}: {e}")
    return None


def extract_data(soup):
    data_dict = {}
    try:
       Typee = soup.find('div', attrs={'id': 'details'}).find('h3').get_text(strip=True)
       Price = soup.find('p', class_='prix').get_text(strip=True)
       data_dict['Type'] = Typee
       data_dict['Price'] = Price
    except:
        print('Error extracting Type and Price.')
    
    # Extracting first part (class 'titre' and 'tag')
    for li in soup.find_all('li'):
        title = li.find('p', class_='titre')
        tag = li.find('p', class_='tag')
        if title and tag:
            key = title.get_text(strip=True)
            value = tag.get_text(strip=True)
            data_dict[key] = value

    # Extracting second part (class 'param' and 'value')
    for li in soup.find_all('li'):
        param = li.find('p', class_='param')
        value = li.find('p', class_='value')
        if param and value:
            key = param.get_text(strip=True)
            value = value.get_text(strip=True)
            data_dict[key] = value

    return data_dict

keys_of_interest = ['Type','Price','Modèle', 'Ville', 'Vendeur', 'Main', 'Kilométrage', 'Carburant', 'Transmision', 'Année de mise en circulation', 'Motorisation', 'Puissance fiscale', 'Puissance dynamique']

df = pd.read_excel('Link wandaloo.xlsx')
links = df['Links'].tolist()

def fetch_and_extract(link):
    soup = get_data(link)
    if soup:
        scraped_data = extract_data(soup)
        return {key: scraped_data[key] for key in keys_of_interest if key in scraped_data}
    return {}

import logging

# Setup logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch_and_extract, link) for link in links]
    results = []
    for future in as_completed(futures):
        try:
            result = future.result()
            if result:
                results.append(result)
        except Exception as exc:
            logging.error(f'Error in thread: {exc}')

df_res = pd.DataFrame(results)
df_res.to_excel('data_wandaloo_ma.xlsx')


