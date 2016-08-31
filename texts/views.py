from django.http import HttpResponse
import os
from twilio.rest import TwilioRestClient
import twilio.twiml

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = TwilioRestClient(account_sid, auth_token)

def index(request):
    return HttpResponse("Hello, world. You're at the texts index.")

def reply(request):
    print(request.body)
    return HttpResponse("")
