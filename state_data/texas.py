from constants import urls
from mail import build
from helpers import excel, translators, filters

def texas_mail():
  # get the texas warn data spreadsheet
  texas_data = excel.get_warn_excel(urls.EXCEL['Texas'], 'texas')

  # translate data to easily iterable format
  warn_data = {}
  warn_data['Texas'] = translators.translate_state_data(texas_data, 'JOB_SITE_NAME', 'WFDD_RECEIVED_DATE', 'LayOff_Date', 'TOTAL_LAYOFF_NUMBER', 'CITY_NAME')

  # filter the data by companies that laid off 100 or more employees
  # large_layoff_data = filters.filter_by_layoff_num(warn_data, 'Texas')
  # convert 100 list to html
  # filtered_html = build.build_html(large_layoff_data, 'Texas', True)

  # filter the data by notices submitted in the past week
  past_week_data = filters.filter_by_past_week(warn_data, 'Texas')
  # check if there is no new data
  if (len(past_week_data['Texas']) == 0):
    past_week_html = build.send_no_data('Texas')
  else:
    # convert past week list to html
    past_week_html = build.build_week_html(past_week_data, 'Texas')

  # convert full list to html
  # full_html = build.build_html(warn_data, 'Texas', False)

  # return full_html
  # return filtered_html
  return past_week_html