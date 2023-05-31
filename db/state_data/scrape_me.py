from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as DT
import math
from constants.urls import me
from helpers.find_last_page import find_last_page

def get_maine_data():
    url = find_last_page(me)
    maine_db = []

    count = 1
    while True:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")

        warn_data = pd.read_html(page.text)
        warn_data = warn_data[0].to_dict()
        
        for idx in reversed(warn_data["Reporting State"]):
            if (warn_data["Reporting State"][idx] == "Maine"):
                temp_data = {}
                temp_data['id'] = count
                count += 1
                temp_data["state"] = "Maine"
                temp_data["location"] = "NULL"
                temp_data["company"] = warn_data["Name"][idx]

                if ('.' in warn_data["Notice Date"][idx]):
                    temp = warn_data["Notice Date"][idx]
                    if ('Sept' in warn_data["Notice Date"][idx]):
                        temp = temp.replace('t', '')
                    temp = temp.replace('.', '')
                    temp_data["date_filed"] = DT.datetime.strptime(temp, '%b %d, %Y')
                else:
                    temp_data["date_filed"] = DT.datetime.strptime(warn_data["Notice Date"][idx], '%B %d, %Y')

                temp_data["date_filed"] = DT.datetime.strftime(temp_data["date_filed"], '%Y-%m-%d')

                if (not isinstance((warn_data["Starting Date"][idx]), str) and math.isnan(warn_data["Starting Date"][idx])):
                    date = DT.datetime.strptime(temp_data["date_filed"], '%Y-%m-%d')
                    temp_data["date_effective"] = date + DT.timedelta(days = 60)
                elif ('.' in warn_data["Starting Date"][idx]):
                    temp = warn_data["Starting Date"][idx]
                    if ('Sept' in warn_data["Starting Date"][idx]):
                        temp = temp.replace('t', '')
                    temp = temp.replace('.', '')
                    temp_data["date_effective"] = DT.datetime.strptime(temp, '%b %d, %Y')
                else:
                    temp_data["date_effective"] = DT.datetime.strptime(warn_data["Starting Date"][idx], '%B %d, %Y')

                if (temp_data["date_effective"] != "NULL"):
                    temp_data["date_effective"] = DT.datetime.strftime(temp_data["date_effective"], '%Y-%m-%d')

                if (math.isnan(warn_data["Number of employees affected"][idx])):
                    temp_data["employee_count"] = "NULL"
                else:
                    temp_data["employee_count"] = math.floor(warn_data["Number of employees affected"][idx])

                maine_db.append(temp_data)

        next_page_element = soup.find("a", {"aria-label": "Previous"})
        if next_page_element:
            next_page_url = next_page_element.get('href')
            url = urljoin(url, next_page_url)
        else:
            break

    print('Maine scrape successfull........')
    return maine_db