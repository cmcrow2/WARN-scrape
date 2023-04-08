from pandas import *
import requests
url = "https://twc.texas.gov/files/news/warn-act-listings-2023-twc.xlsx"

res = requests.get(url)
open('temp.xls', 'wb').write(res.content)

xls = ExcelFile('temp.xls')
warn_data = xls.parse(xls.sheet_names[0])
print(warn_data.to_dict())
