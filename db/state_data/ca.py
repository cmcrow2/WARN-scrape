import csv
from helpers.date import uniform_date_string
import os
from dotenv import load_dotenv
load_dotenv()

def get_ca_data():
    path = os.getenv('CSV_PATH')
    data = []

    reader = csv.DictReader(open(path + '/ca.csv'))
    for row in reader:
        temp_data = {}

        temp_data["state"] = "California"
        temp_data["location"] = row["county"]
        temp_data["company"] = row["company"]
        temp_data["date_filed"] = uniform_date_string(row["received_date"])
        temp_data["date_effective"] = uniform_date_string(row["effective_date"])
        
        if (row["num_employees"] == ''):
            temp_data["employee_count"] = "NULL"
        else:
            temp_data["employee_count"] = int(row["num_employees"].replace(',', ''))

        data.append(temp_data)

    return data