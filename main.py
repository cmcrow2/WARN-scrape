from mail import send_email
from state_data import texas

# grab texas html
texas_html = texas.texas_mail()

# use email library to send html to devs
send_email.send_email(texas_html)
