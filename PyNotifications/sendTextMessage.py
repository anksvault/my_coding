#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Vashistha                                           #
# Script      : sendTextMessage.py                                        #
# Py Versions : 3.5                                                       #
# Required    : twilio, authenticateAccount                               #
# Execute     : python sendTextMessage.py                                 #
#=========================================================================#

import twilio
import twilio.rest
import authenticateAccount as aa

try:
    client = twilio.rest.TwilioRestClient(aa.account_sid, aa.auth_token)

    message = client.messages.create(
        body="Your SMS Text Here",
        to="",    # Number Format: +10123456789
        from_=""  # Number Format: +10123456789
    )
except twilio.TwilioRestException as e:
    print e