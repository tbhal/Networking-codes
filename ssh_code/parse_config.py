from paramiko.client import SSHClient
from paramiko import SSHConfig

SSH_CONFIG = input("Insert path to ssh config")
SSH_HOST = input("Name of host")

client = SSHClient()
config = SSHConfig()

# load and parse config file
config_file = open(SSH_CONFIG)
config.parse(config_file)

# performing lookup for extracting stored info in the cnonfiguration
# lookup will return dictionary
dev_config = config.lookup(SSH_HOST)

client.load_host_keys()
HOST = dev_config['hostname']
client.connect(HOST, port=int(dev_config['port']),
username=dev_config['user'], key_filename=dev_config['identityfile'])
client.close()