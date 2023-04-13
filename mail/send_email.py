from dotenv import load_dotenv
import os
from email.message import EmailMessage
import ssl
import smtplib
load_dotenv()

def send_email(body):
  email_sender = '19ccrow99@gmail.com'
  email_password = os.getenv('PASS')
  # email_receiver = ['19ccrow99@gmail.com', 'dpinargo@gmail.com']
  email_receiver = '19ccrow99@gmail.com'

  subject = '2023 WARN Data for Texas'

  em = EmailMessage()
  em['From'] = email_sender
  em['To'] = email_receiver
  em['Subject'] = subject
  em.set_content(body, subtype='html')

  context = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
      smtp.login(email_sender, email_password)
      smtp.sendmail(email_sender, email_receiver, em.as_string())