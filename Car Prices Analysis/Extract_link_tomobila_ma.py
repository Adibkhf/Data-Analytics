import re
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import requests
import concurrent
import pandas as pd

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        return None

def process_page(page_number):
    url = f"https://www.tomobila.ma/achat-voiture-occasion/page/{page_number}/"
    soup = get_data(url)
    car_data = []
    
    if soup:
        for x in soup.findAll('div', attrs={'class': 'content'}):
            car_info = {}

            # Extracting price
            price = x.find('span', attrs={'class': 'heading-font'})
            if price:
                car_info['Price'] = price.get_text().strip()

            # Extracting link
            link = x.find('a', attrs={'class': 'rmv_txt_drctn'})
            if link:
                car_info['Link'] = link.get('href').strip()

            # Extracting type
            typee = x.find('a', attrs={'class': 'rmv_txt_drctn'})
            if typee:
                car_info['Type'] = typee.get_text().strip()

            # Extracting kilometrage
            regex = r"(\d+\s?km)"
            txt = x.get_text()
            km = re.findall(regex, txt)
            if km:
                car_info['Km'] = km[0].strip()
       

            if car_info:
                car_data.append(car_info)
            
    return car_data


results = []
with ThreadPoolExecutor(max_workers=10) as executor:
    # Adjust the range as needed
    future_to_url = {executor.submit(process_page, page_number): page_number for page_number in range(1, 1288)}
    for future in concurrent.futures.as_completed(future_to_url):
        results.extend(future.result())


df = pd.DataFrame(results)

df.to_excel('Link tomobila_ma.xlsx')