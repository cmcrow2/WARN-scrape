import pandas as pd
import requests
import datetime as DT
from constants.urls import al

def get_alabama_data():
    page = requests.get(al)

    warn_data = pd.read_html(page.text)
    warn_data = warn_data[0].to_dict()

    alabama_db = []

    count = 1
    for idx in range(len(warn_data["Initial Report Date"]) - 1, -1, -1):
        temp_data = {}
        temp_data['id'] = count
        count += 1
        temp_data["state"] = "Alabama"
        temp_data["location"] = warn_data["City"][idx]
        temp_data["company"] = warn_data["Company"][idx]

        date = DT.datetime.strptime(warn_data["Initial Report Date"][idx], '%m/%d/%Y')
        temp_data["date_filed"] = DT.datetime.strftime(date, '%Y-%m-%d')

        date = DT.datetime.strptime(warn_data["Planned Starting Date"][idx], '%m/%d/%Y')
        temp_data["date_effective"] = DT.datetime.strftime(date, '%Y-%m-%d')

        temp_data["employee_count"] = warn_data["Planned # Affected Employees"][idx]

        alabama_db.append(temp_data)

    print('Alabama scrape successfull........')
    return alabama_db
