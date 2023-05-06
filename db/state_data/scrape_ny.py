import pandas as pd
import requests
import datetime as DT

def get_newyork_data():
    page = requests.get('https://dol.ny.gov/warn-notices')

    warn_data = pd.read_html(page.text)
    warn_data = warn_data[0].to_dict()

    newyork_db = []

    for idx in range(0, len(warn_data["Date Posted"])):
        temp_data = {}
        temp_data["state"] = "New York"
        temp_data["location"] = "NULL"
        temp_data["company"] = warn_data["Company Name"][idx]

        if ('amended' in warn_data["Date Posted"][idx].lower()):
            temp_data["date_filed"] = warn_data["Date Posted"][idx].split(' ')[0]
            temp_data["date_filed"] = DT.datetime.strptime(temp_data["date_filed"], '%m/%d/%Y')
            temp_data["date_filed"] = DT.datetime.strftime(temp_data["date_filed"], '%Y-%m-%d')
        else:
            temp_data["date_filed"] = DT.datetime.strptime(warn_data["Date Posted"][idx], '%m/%d/%Y')
            temp_data["date_filed"] = DT.datetime.strftime(temp_data["date_filed"], '%Y-%m-%d')

        temp_data["date_effective"] = "NULL"
        temp_data["employee_count"] = "NULL"

        newyork_db.append(temp_data)

    return newyork_db
