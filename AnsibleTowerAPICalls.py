#!/usr/bin/python

#================================================================================#
# Author      : Ankit Vashistha                                                  #
# Script      : AnsibleTowerAPICalls.py                                          #
# Py Versions : 2.7, 3.5                                                         #
# Required    : requests, getpass, base64, requests.packages.urllib3.exceptions  #
# Execute     : python MSTeamsNotifications.py                                   #
#================================================================================#

#import urllib3  # Use in case of invalid certificate warning.
import requests
import getpass
import base64
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#un = base64.b64decode("")
#pw = base64.b64decode("")

un = raw_input("Enter your username: ")
pw = getpass.getpass("[NO-ECHO] Enter your password: ")


# Disable API Warnings for self signed certificate.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


getAPIlist = requests.get('https://<tower_host>/api/v2/', auth=(un, pw), verify=False)
dictAPIlistvalues=dict(getAPIlist.json())

# Prints API v2 Options.
print("Hello "+ un +"Following are the resources which are accessing for your credentials:\n")
print("KEY      :      Value")
print("---------------------")

for i in dictAPIlistvalues:
    print(i+" : "+dictAPIlistvalues[i])


getResult = requests.get('https://<tower_host>/api/v2/hosts/114/ansible_facts/', auth=(un, pw), verify=False)
dictAPIResult=dict(getResult.json())

print("Ansible Tower Hosts Details Accessible for you: \n")
print("KEY      :      Value")
print("---------------------")
