import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_warn_scrape(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.text, 'lxml')
  table = soup.find('table')
  headers = []
  for i in table.find_all('th'):
      title = i.text
      headers.append(title)

  state_data = pd.DataFrame(columns = headers)
  for j in table.find_all('tr')[1:]:
      row_data = j.find_all('td')
      row = [i.text for i in row_data]
      length = len(state_data)
      state_data.loc[length] = row

  state_data = state_data.to_dict()

  return state_data