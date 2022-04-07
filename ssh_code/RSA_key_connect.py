# connect to ssh server using the keys
# for this the intended server needs to be configured for the same

from idna import valid_contextj
from paramiko.client import SSHClient
import getpass

SSH_USER = input('Username: ')
SSH_HOST = input('Host: ')
SSH_PORT = int(input('Port: '))
SSH_KEY = input("Name of your private key")
SSH_KEY_PASS = getpass.getpass(prompt="Password: ")
CMD = input("Enter command you want to execute")

client = SSHClient()

client.load_host_keys()
client.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER,
look_for_keys=True, key_filename=SSH_KEY, passphrase=SSH_KEY_PASS)

stdin, stdout, stderr = client.exec_command(CMD)
client.close()

# there might be the case that thekey is present in some othe directory
# we can directly pass the directoy in which we have to look
# in the SSH_KEY parameter, or a list can be provided, for that
# we have traverse them in that case