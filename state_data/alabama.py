import requests
from bs4 import BeautifulSoup
import pandas as pd
from constants import urls
from mail import build
from helpers import excel, translators, filters

def alabama_mail():
    page = requests.get(urls.SCRAPE['Alabama'])
    soup = BeautifulSoup(page.text, 'lxml')
    table = soup.find('table')
    headers = []
    for i in table.find_all('th'):
        title = i.text
        headers.append(title)

    alabama_data = pd.DataFrame(columns = headers)
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(alabama_data)
        alabama_data.loc[length] = row
    
    alabama_data = alabama_data.to_dict()
    warn_data = {}
    warn_data['Alabama'] = translators.translate_state_data(alabama_data, 'Company', 'Initial Report Date', 'Planned Starting Date', 'Planned # Affected Employees', 'City')
    
    # filter the data by notices submitted in the past week
    past_week_data = filters.filter_by_past_week(warn_data, 'Alabama')
    # check if there is no new data
    if (len(past_week_data['Alabama']) == 0):
      past_week_html = build.send_no_data('Alabama')
    else:
      # convert past week list to html
      past_week_html = build.build_week_html(past_week_data, 'Alabama')

    # full_html = build.build_html(warn_data, 'Alabama', False)

    # return full_html
    return past_week_html
    