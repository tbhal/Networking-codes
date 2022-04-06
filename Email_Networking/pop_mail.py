# Get new mails in mailbox


import poplib
import getpass

mailbox = poplib.POP3_SSL("pop.gmail.com", 995)

username = input("Username: ")
Password = getpass.getpass(prompt="Password: ")

mailbox.user(username)
mailbox.pass_(Password)


EmailInformation = mailbox.stat()
print("Number of new emails %s" % EmailInformation)

numberOfMails = EmailInformation[0]

num_messages = len(mailbox.list()[1])

for i in range(num_messages):
    print("\nMessage Number " + str(i+1))
    print("--"*25)

    # reading the message
    response, headerLines, bytes = mailbox.retr(i+1)
    print('Message ID: ', headerLines[1])
    print('Date ', headerLines[2])
    print('Reply To ', headerLines[4])
    print('To ', headerLines[5])
    print('Subject ', headerLines[6])
    print('MIME ', headerLines[7])
    print('Content Type ', headerLines[8])

mailbox.quit()