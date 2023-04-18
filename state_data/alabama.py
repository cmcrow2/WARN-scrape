from constants import urls
from mail import build
from helpers import scrape, translators, filters

def alabama_mail():
    # get the alabama warn data
    alabama_data = scrape.get_warn_scrape(urls.SCRAPE['Alabama'])

    # translate data to easily iterable format
    warn_data = {}
    warn_data['Alabama'] = translators.translate_state_data(alabama_data, 'Company', 'Initial Report Date', 'Planned Starting Date', 'Planned # Affected Employees', 'City')
    
    # filter the data by notices submitted in the past week
    past_week_data = filters.filter_by_past_week(warn_data, 'Alabama')
    # check if there is no new data
    if (len(past_week_data['Alabama']) == 0):
      past_week_html = build.send_no_data('Alabama')
    else:
      # convert past week list to html
      past_week_html = build.build_week_html(past_week_data, 'Alabama')

    return past_week_html
    