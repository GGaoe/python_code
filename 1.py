import requests
import time
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('Error')
        return ''
    
def get_url(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = []
    for link in soup.find_all('a'):
        try:
            urls.append(link.get('href'))
        except:
            print('Error')
    return urls