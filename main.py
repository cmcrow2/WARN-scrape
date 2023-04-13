from pandas import *
import requests
from dotenv import load_dotenv
import os
from email.message import EmailMessage
import ssl
import smtplib
url = "https://twc.texas.gov/files/news/warn-act-listings-2023-twc.xlsx"
load_dotenv()

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

# convert 100 list to html
partial_html = "<h2>Texas WARN Notices:</h2>"
partial_html += "<table><tr>"
partial_html += "<th>Company</th>"
partial_html += "<th>City</th>"
partial_html += "<th>Date Posted</th>"
partial_html += "<th>Date Layoffs Begin</th>"
partial_html += "<th>Number of Layoffs</th>"
partial_html += "</tr>"

for index in range(len(large_layoff_data["Texas"])):
    temp_company = large_layoff_data["Texas"][index]["company"]
    temp_city = large_layoff_data["Texas"][index]["city"]
    temp_date_posted = large_layoff_data["Texas"][index]["date_posted"]
    temp_layoff_date = large_layoff_data["Texas"][index]["layoff_date"]
    temp_layoff_number = large_layoff_data["Texas"][index]["layoff_number"]
    
    partial_html += "<tr>"
    partial_html += f"<td>{temp_company}</td>"
    partial_html += f"<td>{temp_city}</td>"
    partial_html += f"<td>{temp_date_posted}</td>"
    partial_html += f"<td>{temp_layoff_date}</td>"
    partial_html += f"<td>{temp_layoff_number}</td>"
    partial_html += "</tr>"

partial_html += "</table>"

# convert full list to html TODO

# combine html
html = "<html><head><style>table {font-family: arial, sans-serif;border-collapse: collapse;width: 100%;}"
html += "td, th {border: 1px solid #dddddd;text-align: left;padding: 8px;}"
html += "p {font-family: arial, sans-serif;font-size: 18px}"
html += "tr:nth-child(even) {background-color: #dddddd;}</style></head><body>"
html += "<p>This is an auto-generated notification detailing companies that are planning to lay off 100 or more employees in 2023.</p>"
html += partial_html
html += "</body></html>"

# use email library to send full html to devs
email_sender = "19ccrow99@gmail.com"
email_password = os.getenv("PASS")
# email_receiver = ["19ccrow99@gmail.com", "dpinargo@gmail.com"]
email_receiver = "19ccrow99@gmail.com"

subject = "2023 WARN Data for Texas"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["Subject"] = subject
em.set_content(html, subtype="html")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
