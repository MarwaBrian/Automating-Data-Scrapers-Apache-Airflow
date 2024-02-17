import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html

def extract(page):
    # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.15'}
    url = f'https://www.buyrentkenya.com/houses-for-rent?page={page}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div', class_='listing-card')
    joblist = []
    elements = ['h2 a', ]
    for item in divs:
            title_element = item.select_one('h2 a')
            title = title_element.text.strip() if title_element else "Title not found"
            print(title)

            job = {
                'title': title,
                # 'item_name':item_name,
                # 'itemPrice': itemPrice,
            }

            joblist.append(job)
    return joblist

pages = []
for i in range(0, 100, 10):
    c = extract(i)
    pages.append(transform(c))


df = pd.DataFrame(pages)
df.to_csv('jobs.csv')
