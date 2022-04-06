# create an SFTP object to connect to the server
# Login to account
# Define headers for the message and login credentials
# Create MIMEMultipart message object
# Attach the message to the MIMEMultipart object
# Send the message

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydoc import plain
import smtplib
import getpass
from ssl import _PasswordType

message = MIMEMultipart() #object created

username = input('Username: ')
Password = getpass.getpass(prompt="Password: ")
reciever = input("Enter reciever email: ")
subject = input("Enter the subject: ")
body = input("Enter email content: ")


message['From'] = username
message['To'] = reciever
message['Subject'] = subject

message.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smpt.gmail.com: 587')
server.starttls()

server.login(message['From'], Password)

server.sendmail(message['From'],message['To'], message.as_string())
print("Mail sent")
server.quit()