import csv
import os
from dotenv import load_dotenv
load_dotenv()

def get_tx_data():
    path = os.getenv('CSV_PATH')
    data = []

    reader = csv.DictReader(open(path + '/tx.csv'))
    for row in reader:
        temp_data = {}

        temp_data["state"] = "Texas"
        temp_data["location"] = row["CITY_NAME"]
        temp_data["company"] = row["JOB_SITE_NAME"]
        temp_data["date_filed"] = row["NOTICE_DATE"].split(' ')[0]
        temp_data["date_effective"] = row["LayOff_Date"].split(' ')[0]
        
        if (row["TOTAL_LAYOFF_NUMBER"] == ''):
            temp_data["employee_count"] = "NULL"
        else:
            temp_data["employee_count"] = int(row["TOTAL_LAYOFF_NUMBER"])

        data.append(temp_data)

    return data