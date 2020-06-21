import requests
from bs4 import BeautifulSoup
import lxml
import time
import random


session = requests.Session()
session.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            'Accept-Language': 'ru',
        }
url = 'https://www.avito.ru/kostroma/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg'
# r = session.get(url)
# r.encoding = r.apparent_encoding
# soup = BeautifulSoup(r.content, 'lxml')

def get_soup(url):
    r = session.get(url)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.content, 'lxml')
    return soup


def get_links_from_page(url_f):
    links_from_page = []
    for i in get_soup(url_f).find_all('a', class_='snippet-link'):
        links_from_page.append('https://www.avito.ru' + i['href'])
    return links_from_page


def get_max_page(soup):
    pagination = []
    for i in soup.find_all('span', class_='pagination-item-1WyVp'):
        pagination.append(i.text)
    max_page = int(pagination[-2])
    return max_page


def get_pages(url):
    pages = []
    for i in range(1, get_max_page(get_soup(url)) + 1):
        pages.append(url + f'?p={i}')
    return pages



# for i in  get_pages(url):
#     print(i)

test = []
for i in get_pages(url):
    test.append(get_links_from_page(i))

all_links = []
for i in test:
    for j in i:
        if j not in all_links:
            all_links.append(j)

print(len(all_links))

