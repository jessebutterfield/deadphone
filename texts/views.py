from django.http import HttpResponse
import os
from twilio.rest import TwilioRestClient
import twilio.twiml
from django.conf import settings

client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID, token=settings.TWILIO_AUTH_TOKEN)

def index(request):
    return HttpResponse("Hello, world. You're at the texts index.")

def reply(request):
    print(request.body)
    return HttpResponse("")
