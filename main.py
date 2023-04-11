from pandas import *
import requests
url = "https://twc.texas.gov/files/news/warn-act-listings-2023-twc.xlsx"

# get the texas warn data spreadsheet
res = requests.get(url)
open('temp.xls', 'wb').write(res.content)

xls = ExcelFile('temp.xls')
texas_data = xls.parse(xls.sheet_names[0])
texas_data = texas_data.to_dict()

# translate data to easily iterable format
warn_data = {}
state_data = []
temp_data = {}

for index in reversed(range(0, len(texas_data["NOTICE_DATE"]))):
    temp_data["company"] = texas_data["JOB_SITE_NAME"][index]
    temp_data["date_posted"] = texas_data["NOTICE_DATE"][index].strftime('%m/%d/%y')
    temp_data["layoff_date"] = texas_data["LayOff_Date"][index].strftime('%m/%d/%y')
    temp_data["layoff_number"] = texas_data["TOTAL_LAYOFF_NUMBER"][index]
    temp_data["city"] = texas_data["CITY_NAME"][index]
    state_data.append(temp_data)
    temp_data = {}

warn_data["Texas"] = state_data

# filter the data by companies that laid off 100 or more employees
large_layoff_data = {
    "Texas": []
}

for index in range(0, len(warn_data["Texas"])):
    if (warn_data["Texas"][index]["layoff_number"] >= 100):
        large_layoff_data["Texas"].append(warn_data["Texas"][index])
