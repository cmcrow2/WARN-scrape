from mail import send_email
from state_data import texas, alabama, california

# grab html
texas_html = texas.texas_mail()
alabama_html = alabama.alabama_mail()
california_html = california.california_mail()

# use email library to send html to devs
send_email.send_email(texas_html, 'Texas')
send_email.send_email(alabama_html, 'Alabama')
send_email.send_email(california_html, 'California')
