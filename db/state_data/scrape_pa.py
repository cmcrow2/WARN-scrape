from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as DT
import math
from constants.urls import pa

def get_pennsylvania_data():
    url = pa
    pennsylvania_db = []

    while True:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")

        warn_data = pd.read_html(page.text)
        warn_data = warn_data[0].to_dict()
        
        for idx in range(0, len(warn_data["Reporting State"])):
            if (warn_data["Reporting State"][idx] == "Pennsylvania"):
                temp_data = {}
                temp_data["state"] = "Pennsylvania"
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
                    temp_data["date_effective"] = "NULL"
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

                pennsylvania_db.append(temp_data)

        next_page_element = soup.find("a", {"aria-label": "Next"})
        if next_page_element:
            next_page_url = next_page_element.get('href')
            url = urljoin(url, next_page_url)
        else:
            break

    return pennsylvania_db
