import csv
from helpers.date import uniform_date_string

def get_ny_data():
    data = []

    reader = csv.DictReader(open('exports/ny.csv'))
    for row in reader:
        temp_data = {}

        temp_data["state"] = "New York"
        temp_data["location"] = row["City"]
        temp_data["company"] = row["company_name"]
        temp_data["date_filed"] = uniform_date_string(row["notice_dated"].split(' ')[0])
        temp_data["date_effective"] = uniform_date_string(row["Layoff Date"].split(' ')[0])

        if (temp_data["location"] == ""):
            temp_data["location"] = "NULL"
        
        if (temp_data["company"] == ""):
            temp_data["company"] = "NULL"
        
        if (temp_data["date_filed"] == ""):
            temp_data["date_filed"] = "NULL"
        
        if (row["Number Affected"] == ''):
            temp_data["employee_count"] = "NULL"
        else:
            temp_data["employee_count"] = int(row["Number Affected"])

        data.append(temp_data)

    return data