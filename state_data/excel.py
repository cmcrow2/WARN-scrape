from pandas import *
import requests

def get_warn_excel(url):
  res = requests.get(url)
  open('texas2023.xls', 'wb').write(res.content)

  xls = ExcelFile('texas2023.xls')
  texas_data = xls.parse(xls.sheet_names[0])
  texas_data = texas_data.to_dict()

  return texas_data