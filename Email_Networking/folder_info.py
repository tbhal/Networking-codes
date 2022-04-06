from imapclient import IMAPClient
import getpass

username = input('Enter username: ')
password = getpass.getpass(prompt="Enter Password:")

server = IMAPClient('imap.gmailcom', ssl=True)

server.login(username, password)
select_info = server.select_folder('INBOX', readonly=True)

for k, v in list(select_info.items()):
    print('%s: %r' %(k,v))

server.logout()