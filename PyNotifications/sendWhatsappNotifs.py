#!/usr/bin/python

#=========================================================================#
# Author      : Ankit Vashistha                                           #
# Script      : sendWhatsappNotifs.py                                     #
# Py Versions : 3.5                                                       #
# Required    : twilio, authenticateAccount                               #
# Execute     : python sendWhatsappNotifs.py                              #
#=========================================================================#

from twilio.rest import Client
import authenticateAccount as aa

# Autheticate Access
client = Client(aa.account_sid, aa.auth_token)

message = client.messages.create(
                              body='Enter your personalized message here',
                              from_='whatsapp:', # Number Format: +10123456789
                              to='whatsapp:' # Number Format: +10123456789
                          )

print(message.sid)