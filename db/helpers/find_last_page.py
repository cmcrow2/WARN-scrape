from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def find_last_page(url):
    while True:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")
        next_page_element = soup.find("a", {"aria-label": "Last"})
        if next_page_element:
            next_page_url = next_page_element.get('href')
            url = urljoin(url, next_page_url)
        else:
            return url