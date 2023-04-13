from pandas import *
import requests
url = 'https://twc.texas.gov/files/news/warn-act-listings-2023-twc.xlsx'
from mail import send_email, build

# get the texas warn data spreadsheet
def get_warn_excel(url):
  res = requests.get(url)
  open('texas2023.xls', 'wb').write(res.content)

  xls = ExcelFile('texas2023.xls')
  texas_data = xls.parse(xls.sheet_names[0])
  texas_data = texas_data.to_dict()

  return texas_data

# translate data to easily iterable format
def translate_state_data(data):
  state_data = []
  temp_data = {}

  for index in reversed(range(0, len(texas_data['NOTICE_DATE']))):
      temp_data['company'] = texas_data['JOB_SITE_NAME'][index]
      temp_data['date_posted'] = texas_data['NOTICE_DATE'][index].strftime('%m/%d/%y')
      temp_data['layoff_date'] = texas_data['LayOff_Date'][index].strftime('%m/%d/%y')
      temp_data['layoff_number'] = texas_data['TOTAL_LAYOFF_NUMBER'][index]
      temp_data['city'] = texas_data['CITY_NAME'][index]
      state_data.append(temp_data)
      temp_data = {}

  return state_data

# filter the data by companies that laid off 100 or more employees
def filter_by_layoff_num(data, state):
  filtered_data = {
      state: []
  }

  for index in range(0, len(data[state])):
      if (data[state][index]['layoff_number'] >= 100):
          filtered_data[state].append(data[state][index])

  return filtered_data

# convert 100 list to html

# convert full list to html TODO

# add filtered or unfiltered data email header

# use email library to send full html to devs

texas_data = get_warn_excel(url)

warn_data = {}
warn_data['Texas'] = translate_state_data(texas_data)

large_layoff_data = filter_by_layoff_num(warn_data, 'Texas')

filtered_html = build.build_html_table(large_layoff_data, 'Texas')
filtered_html = build.add_header(filtered_html, True)

send_email.send_email(filtered_html)
