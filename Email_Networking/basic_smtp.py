import smtplib

# create smtp object from SMTP class, passing host address and port
smtp = smtplib.SMTP("smtp.gmail.com", 588)

try:
    smtp.sendmail('sendermail', 'recievers mail or list', "This is a test e-mail message")
except smtplib.SMTPException as exception:
    print("Error: unable to send mail"+exception)
finally:
    smtp.quit()