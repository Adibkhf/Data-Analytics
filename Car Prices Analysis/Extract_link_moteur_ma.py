from bs4 import BeautifulSoup
import requests
from concurrent.futures import ThreadPoolExecutor

import concurrent


def get_data(link):
    r = requests.get(link,stream=True,verify = False)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content,'html.parser')
    return soup
    
for x in range(1,934):
    n = x*30
    l = 'https://www.moteur.ma/fr/voiture/achat-voiture-occasion/'+n
    S = get_data(l)
    for x in S.findAll('div',attrs = {'class':"row bloc-info"}):
        try:
            R.append(x.find('a').get('href'))
        except:
            pass
    

def scrape_data(x):
    n = x * 30
    l = f'https://www.moteur.ma/fr/voiture/achat-voiture-occasion/{n}'
    response = requests.get(l)
    S = BeautifulSoup(response.content, 'html.parser')
    links = []
    for item in S.findAll('div', attrs={'class': "row bloc-info"}):
        try:
            link = item.find('a').get('href')
            links.append(link)
        except Exception as e:
            print(f"Error: {e}")
    return links

R = []

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(scrape_data, x) for x in range(1, 934)]
    for future in concurrent.futures.as_completed(futures):
        R.extend(future.result())

res = [[x,'moteur.ma'] for x in R]
import pandas as pd 
df = pd.DataFrame(res,columns=['Link','Source'])
df.to_excel('Liens moteur_ma.xlsx')


    

    
