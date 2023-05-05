from db.select import get_from_db
from mail.build import build_week_html
from mail.send_email import send_email
from warn.scrapers import tx
from warn.scrapers import ca
from warn.scrapers import ny

import os
from dotenv import load_dotenv
load_dotenv()

res = get_from_db()
data = []

for key in res:
    data.append(list(key))

html = build_week_html(data)
send_email(html)
