import pandas as pd
import requests
import datetime as DT
from constants.urls import ut

def get_utah_data():
    page = requests.get(ut)

    warn_data = pd.read_html(page.text)
    warn_data = warn_data[0].to_dict()

    utah_db = []

    for idx in range(0, len(warn_data["Date of Notice"])):
        temp_data = {}
        temp_data["state"] = "Utah"
        temp_data["location"] = warn_data["Location"][idx]
        temp_data["company"] = warn_data["Company Name"][idx]

        date = DT.datetime.strptime(warn_data["Date of Notice"][idx], '%m/%d/%Y')
        temp_data["date_filed"] = DT.datetime.strftime(date, '%Y-%m-%d')

        temp_data["date_effective"] = date + DT.timedelta(days = 60)
        temp_data["date_effective"] = DT.datetime.strftime(temp_data["date_effective"], '%Y-%m-%d')

        temp_data["employee_count"] = warn_data["Affected Workers"][idx]

        utah_db.append(temp_data)

    return utah_db
