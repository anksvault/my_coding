#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Vashistha                                           #
# Script      : MSTeamsSuccessNotification.py                             #
# Py Versions : 2.7                                                       #
# Required    : requests, json, getpass, base64, pprint, HTTPBasicAuth    #
# Execute     : python MSTeamsNotifications.py                            #
#=========================================================================#

import requests
import json
import getpass
import base64
from requests.auth import HTTPBasicAuth

# Uncomment below to accept run time inputs
#un = raw_input("Enter your username: ")
#pw = getpass.getpass("[NO-ECHO] Enter your password: ")

url = ""  # Your Webhook URL.
un = base64.b64decode("") # Your Base64 encoded Username
pw = base64.b64decode("") # Your Base64 encoded Password

print("MSTeamsNotifications.py - Send Notifications to MS Teams Team")

payload = "{\"title\": \"Job Completed Successfully\", \"text\": \"The configuration Job is completed Successfully.\"}"
auth = HTTPBasicAuth(un, pw)

headers = { 'MessageType': "Test" }

response = requests.post(url, data=payload, headers=headers, auth=auth)

print(response.text)
