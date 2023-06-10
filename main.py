from db.get_from_db import get_from_db
from db.update import update_db
from mail.build import build_week_html
from mail.send_email import send_email
from db.constants.state_list import mon_list, tue_list, wed_list, thu_list, fri_list, sat_list, sun_list
import datetime as DT

def build_data(res, state):
    data = []

    for key in res:
        data.append(list(key))

    html = build_week_html(data)
    send_email(html, state)
    print(f'Email Sent for {state}')
    update_db(state)

today = DT.datetime.now()
weekday = today.weekday()

if weekday == 0: curr_list = mon_list
elif weekday == 1: curr_list = tue_list
elif weekday == 2: curr_list = wed_list
elif weekday == 3: curr_list = thu_list
elif weekday == 4: curr_list = fri_list
elif weekday == 5: curr_list = sat_list
elif weekday == 6: curr_list = sun_list

for state in curr_list:
    res = get_from_db(state)
    build_data(res, state)
