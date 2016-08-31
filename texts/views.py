from django.http import HttpResponse
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from texts.models import TwilioNumber, Contact

client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID, token=settings.TWILIO_AUTH_TOKEN)


def index(request):
    return HttpResponse("Hello, world. You're at the texts index.")

@csrf_exempt
def reply(request):
    to = request.POST['To']
    numbers = TwilioNumber.objects.filter(number=to)
    message_body = request.POST['Body']
    target = message_body.split()[0]
    contact = Contact.objects.filter(user=numbers[0], first_name=target)
    message = client.messages.create(to=contact[0], from_=to,
                                     body=message_body)
    number = request.POST['From']
    return HttpResponse("")
