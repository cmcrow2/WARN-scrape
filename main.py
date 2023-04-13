from pandas import *
url = 'https://twc.texas.gov/files/news/warn-act-listings-2023-twc.xlsx'
from mail import send_email, build
from state_data import excel, translators, filters


# get the texas warn data spreadsheet

# translate data to easily iterable format

# filter the data by companies that laid off 100 or more employees

# convert 100 list to html

# convert full list to html TODO

# add filtered or unfiltered data email header

# use email library to send full html to devs

texas_data = excel.get_warn_excel(url)

warn_data = {}
warn_data['Texas'] = translators.translate_state_data(texas_data)

large_layoff_data = filters.filter_by_layoff_num(warn_data, 'Texas')

filtered_html = build.build_html_table(large_layoff_data, 'Texas')
filtered_html = build.add_header(filtered_html, True)

send_email.send_email(filtered_html)
