from db.get_from_db import get_from_db
from db.update import update_db
from mail.build import build_week_html
from mail.send_email import send_email
from db.constants.state_list import state_list

def build_data(res, state):
    data = []

    for key in res:
        data.append(list(key))

    html = build_week_html(data)
    send_email(html, state)
    print(f'Email Sent for {state}')
    update_db(state)


for state in state_list:
    res = get_from_db(state)
    build_data(res, state)
