from db.get_from_db import get_from_db
from mail.build import build_week_html
from mail.send_email import send_email

res = get_from_db()
data = []

for key in res:
    data.append(list(key))

html = build_week_html(data)
send_email(html)
