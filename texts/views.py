from django.http import HttpResponse
import os
from twilio.rest import TwilioRestClient
import twilio.twiml

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
print(account_sid)
print(auth_token)
client = TwilioRestClient(account=account_sid, token=auth_token)

def index(request):
    return HttpResponse("Hello, world. You're at the texts index.")

def reply(request):
    print(request.body)
    return HttpResponse("")
