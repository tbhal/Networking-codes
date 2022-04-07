from paramiko.client import SSHClient
import getpass

SSH_USER = input('Username: ')
SSH_HOST = input('Host: ')
SSH_PASSWORD = getpass.getpass(prompt="Password: ")
SSH_PORT = int(input('Port: '))

client = SSHClient()

client.load_system_host_keys()
try:
    client.connect(SSH_HOST, port=SSH_PORT,
    username=SSH_USER, password=SSH_PASSWORD,
    look_for_keys=False)

    print("Connected successfully")
except Exception:
    print("Failed to establish connection")

finally:
    client.close()