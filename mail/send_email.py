import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv
load_dotenv()

def send_email(body, state):
  email_sender = os.getenv('EMAIL_FROM')
  email_password = os.getenv('PASS')
#   email_receiver = ['19ccrow99@gmail.com', 'dpinargo@gmail.com']
  email_receiver = '19ccrow99@gmail.com'

  subject = f'2023 WARN Data for {state.capitalize()}'

  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email_receiver
  em['Subject'] = subject
  em.set_content(body, subtype='html')

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())