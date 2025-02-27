#!/usr/bin/python3

import requests
import passwords

user = passwords.user
passwd = passwords.passwd
response = requests.get(f"http://172.17.0.1:8080/basic-auth/{user}/{passwd}", auth=(user,passwd))

print(response.status_code)
print(response.text)
