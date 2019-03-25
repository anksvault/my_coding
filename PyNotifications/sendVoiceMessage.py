#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Vashistha                                           #
# Script      : sendVoiceMessage.py                                       #
# Py Versions : 3.5                                                       #
# Required    : twilio, authenticateAccount                               #
# Execute     : python sendVoiceMessage.py                                #
#=========================================================================#

from twilio.rest import Client
import authenticateAccount as aa

# Autheticate Access
client = Client(aa.account_sid, aa.auth_token)

# Send Voice Message with sample template from twilio.
call_response = client.calls.create(
    to="",     # Number Format: +10123456789
    from_="",  # Number Format: +10123456789
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call_response.sid)