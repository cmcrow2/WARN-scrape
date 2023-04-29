import csv

def get_ak_data():
    data = []

    reader = csv.DictReader(open('exports/ak.csv'))
    for row in reader:
        temp_data = {}
        temp_data["state"] = "Alaska"
        temp_data["location"] = row["Location"]
        temp_data["company"] = row["Company"]
        temp_data["date_filed"] = row["Notice Date"]
        temp_data["date_effective"] = row["Layoff Date"]
        if (row["Employees Affected"] == "TBA"):
            temp_data["employee_count"] = int("-1")
        elif ("up to" in row["Employees Affected"].lower()):
            temp_data["employee_count"] = int(row["Employees Affected"].split(' ')[-1])
        else:
            temp_data["employee_count"] = int(row["Employees Affected"].replace(',', ''))
        data.append(temp_data)

    return data