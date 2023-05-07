import datetime as DT

today = DT.datetime.now()
delta = DT.timedelta(days = 7)
week_ago = today - delta
week_ago = DT.datetime.strftime(week_ago, '%Y-%m-%d')

all_data_week = f'''SELECT * FROM state_data
    WHERE date_filed >= '{week_ago}'
    ORDER BY date_filed desc
    '''