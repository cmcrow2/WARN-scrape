from pandas import ExcelFile
import requests
import os
from dotenv import load_dotenv
load_dotenv()

url = "https://twc.texas.gov/files/news/warn-act-listings-2023-twc.xlsx"

def get_texas_data():
    path = os.getenv('CSV_PATH')
    res = requests.get(url)
    open(path + '/texas2023.csv', 'wb').write(res.content)

    xls = ExcelFile(path + '/texas2023.csv')
    warn_data = xls.parse(xls.sheet_names[0])

    texas_db = []

    for idx in range(0, len(warn_data["NOTICE_DATE"])):
        temp_data = {}
        temp_data["state"] = "Texas"
        temp_data["location"] = warn_data["CITY_NAME"][idx]
        if ("   " in warn_data["JOB_SITE_NAME"][idx]):
            temp_data["company"] = "NULL"
        else:
            temp_data["company"] = warn_data["JOB_SITE_NAME"][idx]
        temp_data["date_filed"] = warn_data["NOTICE_DATE"][idx].strftime("%Y-%m-%d")
        temp_data["date_effective"] = warn_data["LayOff_Date"][idx].strftime("%Y-%m-%d")
        temp_data["employee_count"] = warn_data["TOTAL_LAYOFF_NUMBER"][idx]

        texas_db.append(temp_data)

    return texas_db
