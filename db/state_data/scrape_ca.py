from pandas import ExcelFile
import requests
import os
from dotenv import load_dotenv
import datetime as datetime
load_dotenv()

url = "https://edd.ca.gov/siteassets/files/jobs_and_training/warn/warn_report.xlsx"

def get_california_data():
    path = os.getenv('CSV_PATH')
    res = requests.get(url)
    open(path + '/california2023.csv', 'wb').write(res.content)

    xls = ExcelFile(path + '/california2023.csv')
    warn_data = xls.parse(xls.sheet_names[0])
    warn_data = warn_data[: len(warn_data) - 2]

    california_db = []

    for idx in range(0, len(warn_data["Received\nDate"])):
        temp_data = {}
        temp_data["state"] = "California"
        temp_data["location"] = warn_data["County/Parish"][idx]
        temp_data["company"] = warn_data["Company"][idx]
        temp_data["date_filed"] = warn_data["Received\nDate"][idx].strftime("%Y-%m-%d")
        temp_data["date_effective"] = warn_data["Effective \nDate"][idx].strftime("%Y-%m-%d")
        temp_data["employee_count"] = warn_data["No. Of\nEmployees"][idx]

        california_db.append(temp_data)

    return california_db
