from concurrent.futures import ThreadPoolExecutor, as_completed
from bs4 import BeautifulSoup
import requests
import pandas as pd
import logging
# Setup logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

session = requests.Session() 

def get_data(link):
    try:
        r = session.get(link)  # Use session object
        r.raise_for_status()   # To raise exception for HTTP error responses
        content = r.content
        soup = BeautifulSoup(content, 'html.parser')
        return soup
    except Exception as exc:
        logging.error(f'Error fetching {link}: {exc}')
        return None


def extract_data(soup):
    data_dict = {}
    Typee = ''
    Price = ''
    city_element = soup.find('a', href=lambda x: x and 'voiture/achat-voiture-occasion/ville/' in x)
    if city_element:
        city = city_element.text.strip()
    else:
        city = None
    data_dict['City'] = city
    try:
        Typee = soup.find('div',attrs = {'class':'col-md-12 col-sm-12 col-xs-12 text-center ads-detail'}).find('span').get_text()
    except:
        pass
        
    try:
        Price = soup.find('div',attrs = {'class':'color_primary text_bold price-block'}).get_text().replace('\n','')
    except:
        pass
    
    data_dict['Type'] = Typee
    data_dict['Price'] = Price
    for div in soup.find_all('div', class_='detail_line'):
        spans = div.find_all('span')
        if len(spans) >= 2:
            key = spans[0].get_text(strip=True)
            value = spans[1].get_text(strip=True)
            data_dict[key] = value
    
    return data_dict

def fetch_and_extract(l):
    soup = get_data(l)
    return extract_data(soup)


# Load URLs from Excel file
df = pd.read_excel('Link moteur_ma.xlsx')
links = df['Link'].tolist()


# Setup logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

with ThreadPoolExecutor(max_workers=20) as executor:
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
df_res.to_excel('data_moteur_ma.xlsx')
