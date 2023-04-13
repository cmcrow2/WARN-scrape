from pandas import *
import requests
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import ssl
import smtplib
url = 'https://twc.texas.gov/files/news/warn-act-listings-2023-twc.xlsx'
load_dotenv()

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
def filter_by_layoff_num(data):
  filtered_data = {
      'Texas': []
  }

  for index in range(0, len(data['Texas'])):
      if (data['Texas'][index]['layoff_number'] >= 100):
          filtered_data['Texas'].append(data['Texas'][index])

  return filtered_data

# convert 100 list to html
def build_html_table(data):
  table = '<h2>Texas WARN Notices:</h2>'
  table += '<table><tr>'
  table += '<th>Company</th>'
  table += '<th>City</th>'
  table += '<th>Date Posted</th>'
  table += '<th>Date Layoffs Begin</th>'
  table += '<th>Number of Layoffs</th>'
  table += '</tr>'

  for index in range(len(large_layoff_data['Texas'])):
      temp_company = large_layoff_data['Texas'][index]['company']
      temp_city = large_layoff_data['Texas'][index]['city']
      temp_date_posted = large_layoff_data['Texas'][index]['date_posted']
      temp_layoff_date = large_layoff_data['Texas'][index]['layoff_date']
      temp_layoff_number = large_layoff_data['Texas'][index]['layoff_number']
      
      table += '<tr>'
      table += f'<td>{temp_company}</td>'
      table += f'<td>{temp_city}</td>'
      table += f'<td>{temp_date_posted}</td>'
      table += f'<td>{temp_layoff_date}</td>'
      table += f'<td>{temp_layoff_number}</td>'
      table += '</tr>'

  table += '</table>'

  return table

# convert full list to html TODO

# add filtered or unfiltered data email header
def add_header(table, is_filtered):
  header = '<html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}'
  header += 'td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}'
  header += 'p {font-family: arial, sans-serif;font-size: 18px}'
  header += 'tr:nth-child(even) {background-color: #dddddd;}</style></head><body>'
  header += '<p>This is an auto-generated notification detailing companies that are planning to lay off'
  if (is_filtered):
     header += ' 100 or more'
  header += ' employees in 2023.</p>'
  header += table
  header += '</body></html>'

  return header
   

# use email library to send full html to devs
def send_email(body):
  email_sender = '19ccrow99@gmail.com'
  email_password = os.getenv('PASS')
  # email_receiver = ['19ccrow99@gmail.com', 'dpinargo@gmail.com']
  email_receiver = '19ccrow99@gmail.com'

  subject = '2023 WARN Data for Texas'

  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email_receiver
  em['Subject'] = subject
  em.set_content(body, subtype='html')

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())

texas_data = get_warn_excel(url)

warn_data = {}
warn_data['Texas'] = translate_state_data(texas_data)

large_layoff_data = filter_by_layoff_num(warn_data)

filtered_html = build_html_table(large_layoff_data['Texas'])

html = add_header(filtered_html, True)

send_email(html)
