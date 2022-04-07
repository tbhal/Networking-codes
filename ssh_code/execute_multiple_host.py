import json
from paramiko.client import SSHClient

#open the json file
credentials = {}
with open("creds.json") as fh:
    json.load(fh)

CMD = input("Enter the command you want to run: ")
for cred in credentials:
    out_file_name = str(cred['name'])+".txt"
    client = SSHClient()
    client.load_host_keys()
    client.connect(cred['host'], port=cred['port'], username=cred['username'],
    password=cred['password'])

    stdin, stdout, stderr = client.exec_command(CMD)
    out_file = open(out_file_name, "w")
    output = stdout.readlines()
    for line in output:
        out_file.write(line)
    out_file.close()
    client.close()
    print("Executed command on " + cred['name'])
