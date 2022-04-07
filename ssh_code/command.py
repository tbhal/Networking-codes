from paramiko.client import SSHClient
import getpass

SSH_USER = input('Username: ')
SSH_HOST = input('Host: ')
SSH_PASSWORD = getpass.getpass(prompt="Password: ")
SSH_PORT = int(input('Port: '))
CMD = input("Enter command you want to execute")

client = SSHClient()

client.load_system_host_keys()
client.connect(SSH_HOST, port=SSH_PORT,
    username=SSH_USER, password=SSH_PASSWORD)
stdin, stdout, stderr = client.exec_command(CMD)

# writing the result printed to a file
output = stdout.readlines()
with open("output.txt", "w") as out_file:
    for line in output:
        out_file.write(line)

# or use this to directly print it
# for line in output:
#     print(line.strip())

#client.close()