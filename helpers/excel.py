from pandas import ExcelFile
import requests

def get_warn_excel(url, state):
  res = requests.get(url)
  open(f'{state}2023.xls', 'wb').write(res.content)

  xls = ExcelFile(f'{state}2023.xls')
  texas_data = xls.parse(xls.sheet_names[0])
  texas_data = texas_data.to_dict()

  return texas_data