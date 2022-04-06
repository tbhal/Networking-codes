import sys
from imapclient import IMAPClient
import getpass

username = input('Enter username: ')
password = getpass.getpass(prompt="Enter Password:")

server = IMAPClient('map.gmail.com', ssl=True)

try:
    server.login(username,password)

except server.Error as e:
    print('Could not login', e)

print('Capabilities: ', server.capabilities)
print('Listing mailbox:')

data = server.list_folders()

for flags, delimiter, folder_name in data:
    print(' %-30s%s %s' % (' '.join(str(flags)), delimiter,folder_name))

server.logout()