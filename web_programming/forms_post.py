from urllib import response
import requests

data_dictionary = {'customer': 'shar', 'custtel': '32232', 'size': 'large', 'custmai': 'shar@domain.com'}

response = requests.post("http://htppbin.org", data=data_dictionary)

print("HTTP Status Code: "+ str(response.status_code))
if response.status_code == 200:
    print(response.text)