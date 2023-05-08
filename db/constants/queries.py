import datetime as DT

today = DT.datetime.now()
delta = DT.timedelta(days = 7)
week_ago = today - delta
week_ago = DT.datetime.strftime(week_ago, '%Y-%m-%d')

def all_data_week(state):
    return f'''SELECT * FROM {state}
    WHERE date_filed >= '{week_ago}'
    ORDER BY date_filed desc
    '''