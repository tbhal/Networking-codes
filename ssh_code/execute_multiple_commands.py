from paramiko.client import SSHClient
import time
import getpass

SSH_USER = input('Username: ')
SSH_HOST = input('Host: ')
SSH_PASSWORD = getpass.getpass(prompt="Password: ")
SSH_PORT = int(input('Port: '))

client = SSHClient()
client.load_host_keys()
client.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER,
password=SSH_PASSWORD)

# open an interactive shell session and a channel that will
# be used to retrieve output

channel = client.get_transport().open_session()
shell = channel.invoke_shell()

# make a list of commands
commands = [
    "hostname", "pwd", "mkdir hehe"
]

for cmd in commands:
    channel.send(cmd+"\n")
    out = channel.recv(1024)
    print(out)
    time.sleep(1)

client.close()