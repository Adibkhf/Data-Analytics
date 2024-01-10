from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        return None

def scrape_page(page_num):
    url = f'https://www.wandaloo.com/occasion/?marque=0&modele=0&budget=0&categorie=0&moteur=0&transmission=0&equipement=-&ville=0&vendeur=0&abonne=0&za&pg={page_num}'
    S = get_data(url)
    if S:
        return [a_tag['href'] for cls in ['odd', 'even'] for item in S.findAll('li', attrs={'class': cls}) if (a_tag := item.find('a')) and a_tag.has_attr('href')]
    else:
        return []

# Using ThreadPoolExecutor to process pages concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    results = executor.map(scrape_page, range(1, 178))

# Flatten the list of lists
all_links = [link for sublist in results for link in sublist]

# Now 'all_links' contains links from all pages
print(f"Total links extracted: {len(all_links)}")

import pandas as pd 

df = pd.DataFrame(all_links,columns=['Links'])
df.to_excel('Link wandaloo.xlsx')
