from django.http import HttpResponse
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import sys

client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID, token=settings.TWILIO_AUTH_TOKEN)

def index(request):
    return HttpResponse("Hello, world. You're at the texts index.")

@csrf_exempt()
def reply(request):
    print(request.body, file=sys.stderr)
    return HttpResponse("")
