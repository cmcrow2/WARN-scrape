from pandas import ExcelFile
import requests
import os
from constants.urls import tx
from dotenv import load_dotenv
load_dotenv()

def get_texas_data():
    path = os.getenv('CSV_PATH')
    res = requests.get(tx)
    open(path + '/texas2023.csv', 'wb').write(res.content)

    xls = ExcelFile(path + '/texas2023.csv')
    warn_data = xls.parse(xls.sheet_names[0])

    texas_db = []

    count = 1
    for idx in range(len(warn_data["CITY_NAME"]) - 1, -1, -1):
        temp_data = {}
        temp_data['id'] = count
        count += 1
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

    print('Texas scrape successfull........')
    return texas_db
