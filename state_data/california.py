from constants import urls
from mail import build
from helpers import excel, translators, filters

def california_mail():
    california_data = excel.get_warn_excel(urls.EXCEL['California'], 'california')

    # translate data to easily iterable format
    warn_data = {}
    warn_data['California'] = translators.translate_state_data(california_data, 'Company', 'Received\nDate', 'Effective \nDate', 'No. Of\nEmployees', 'County/Parish')
    warn_data['California'] = warn_data['California'][2:]

    # filter the data by notices submitted in the past week
    past_week_data = filters.filter_by_past_week(warn_data, 'California')
    # check if there is no new data
    if (len(past_week_data['California']) == 0):
      past_week_html = build.send_no_data('California')
    else:
      # convert past week list to html
      past_week_html = build.build_week_html(past_week_data, 'California')

    # full_html = build.build_html(warn_data, 'California', False)
    
    # return full_html
    return past_week_html
