from constants import urls
from mail import send_email, build
from state_data import excel, translators, filters

# get the texas warn data spreadsheet
texas_data = excel.get_warn_excel(urls.TEXAS_URL)

# translate data to easily iterable format
warn_data = {}
warn_data['Texas'] = translators.translate_state_data(texas_data)

# filter the data by companies that laid off 100 or more employees
large_layoff_data = filters.filter_by_layoff_num(warn_data, 'Texas')
# convert 100 list to html
filtered_html = build.build_html(large_layoff_data, 'Texas', True)

# filter the data by notices submitted in the past week
past_week_data = filters.filter_by_past_week(warn_data, 'Texas')
# convert past week list to html
past_week_html = build.build_week_html(past_week_data, 'Texas')


# convert full list to html
full_html = build.build_html(warn_data, 'Texas', False)


# use email library to send html to devs (uncomment to test)
# send_email.send_email(filtered_html)
# send_email.send_email(full_html)
send_email.send_email(past_week_html)
