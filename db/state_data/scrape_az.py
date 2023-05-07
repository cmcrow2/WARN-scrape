import pandas as pd
import requests
import datetime as DT
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import pandas as pd
from constants.urls import az

def get_arizona_data():
    url = az
    arizona_db = []

    while True:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")

        warn_data = pd.read_html(page.text)
        warn_data = warn_data[0].to_dict()

        for idx in range(0, len(warn_data["Notice Date"])):
            temp_data = {}
            temp_data["state"] = "Arizona"
            temp_data["location"] = warn_data["ZIP"][idx]
            temp_data["company"] = warn_data["Employer"][idx]

            temp_data["date_filed"] = DT.datetime.strptime(warn_data["Notice Date"][idx], '%b %d, %Y')
            temp_data["date_filed"] = DT.datetime.strftime(temp_data["date_filed"], '%Y-%m-%d')

            temp_data["date_effective"] = "NULL"
            temp_data["employee_count"] = "NULL"

            arizona_db.append(temp_data)

        next_page_element = soup.select_one("a.next_page")
        if next_page_element:
            next_page_url = next_page_element.get('href')
            url = urljoin(url, next_page_url)
        else:
            break

    return arizona_db
