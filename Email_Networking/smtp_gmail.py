from ssl import _PasswordType
import sys, smtplib, socket

from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from typing import final
import getpass

sender_mail = input("Enter senders mail")
password = getpass.getpass(prompt='Password: ')
try:
    msg = MIMEText("Message 1 say HI bhai", 'plain')
    msg['Subject'] = "Mesage for Tushar"
    msg['From'] = sender_mail

    smtp = smtplib.SMTP("smtp.gmail.com", 587)
    smtp.set_debuglevel(True)
    smtp.ehlo() # to identify ourself as client

    if smtp.has_extn('STARTTLS'):
        smtp.starttls()
        smtp.ehlo()
    
 #credentials section   
    try:
        smtp.login(sender_mail, password)
    except smtplib.SMTPException as e:
        print("Authentication error", e)
        sys.exit()

# sending mail
    try:
        smtp.sendmail(sender_mail, ['tushar.rocks97@gmail.com'], msg.as_string())
    except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
        print("Your message has not been sent")
        print(e)
        sys.exit(1)
    finally:
        smtp.quit()

except(socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print("Message has not been sent")
    print(e)
    sys.exit(1)