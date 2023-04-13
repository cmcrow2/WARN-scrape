url = 'https://twc.texas.gov/files/news/warn-act-listings-2023-twc.xlsx'
from mail import send_email, build
from state_data import excel, translators, filters


# get the texas warn data spreadsheet
texas_data = excel.get_warn_excel(url)

# translate data to easily iterable format
warn_data = {}
warn_data['Texas'] = translators.translate_state_data(texas_data)

# filter the data by companies that laid off 100 or more employees
large_layoff_data = filters.filter_by_layoff_num(warn_data, 'Texas')

# convert 100 list to html
filtered_html = build.build_html_table(large_layoff_data, 'Texas')
filtered_html = build.add_header(filtered_html, True)

# convert full list to html TODO
full_html = build.build_html_table(warn_data, 'Texas')
full_html = build.add_header(full_html, False)

# use email library to send full html to devs
send_email.send_email(filtered_html)
send_email.send_email(full_html)
