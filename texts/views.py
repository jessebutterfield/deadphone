from django.http import HttpResponse
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import sys

client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID, token=settings.TWILIO_AUTH_TOKEN)


def index(request):
    if not request.user.is_authenticated():
        print(request.META)
        return HttpResponse('', status=401)
    print(request.user)
    return HttpResponse("Hello, world. You're at the texts index.")

@csrf_exempt
def reply(request):
    if not request.user.is_authenticated:
        return HttpResponse('', status=401)
    return HttpResponse("")
