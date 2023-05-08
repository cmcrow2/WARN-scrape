import pandas as pd
import requests
import datetime as DT
from constants.urls import oh

def get_ohio_data():
    page = requests.get(oh)

    warn_data = pd.read_html(page.text, match='Company')
    warn_data = warn_data[0].to_dict()

    ohio_db = []

    count = 1
    for idx in reversed(warn_data["Date Received"]):
        temp_data = {}

        temp_data['id'] = count
        count += 1

        temp_data["state"] = "Ohio"

        temp_data["location"] = warn_data["City/County"][idx]

        temp_data["company"] = warn_data["Company"][idx]

        temp_data["date_filed"] = DT.datetime.strptime(warn_data["Date Received"][idx].split(' ')[-1], '%m/%d/%Y')
        temp_data["date_filed"] = DT.datetime.strftime(temp_data["date_filed"], '%Y-%m-%d')

        temp_data["date_effective"] = warn_data["Layoff Date(s)"][idx].split(' ')[0]
        temp_data["date_effective"] = DT.datetime.strptime(temp_data["date_effective"], '%m/%d/%Y')
        temp_data["date_effective"] = DT.datetime.strftime(temp_data["date_effective"], '%Y-%m-%d')

        if ("Unknown" in warn_data["Potential Number Affected"][idx]):
            temp_data["employee_count"] = "NULL"
        else:
            temp_data["employee_count"] = warn_data["Potential Number Affected"][idx]

        ohio_db.append(temp_data)

    return ohio_db
