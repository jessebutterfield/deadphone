from django.http import HttpResponse
from twilio.rest import TwilioRestClient
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from texts.models import TwilioNumber, Contact, Conversation

client = TwilioRestClient(account=settings.TWILIO_ACCOUNT_SID, token=settings.TWILIO_AUTH_TOKEN)


def index(request):
    return HttpResponse("Hello, world. You're at the texts index.")

@csrf_exempt
def reply(request):
    to = request.POST['To']
    numbers = TwilioNumber.objects.filter(number=to)
    if len(numbers) < 1:
        return HttpResponse('Not a number registered to deadphone', status=400)
    user = numbers[0].user
    number = request.POST['From']
    message_body = request.POST['Body']
    convo = Conversation.objects.filter(to_phone=number, user=user, expires_at__gte=datetime.now())
    if len(convo) > 0:
        client.messages.create(to=convo[0].from_phone, from_=to,
                                     body=message_body)
        return HttpResponse("")
    if message_body.starts_with('@'):
        target = message_body.split()[0][1:]
        contacts = Contact.objects.filter(user=user, first_name=target)
        #TODO: this should text back that the user is unknown or a set of close
        #possiblities
        if len(contacts) < 1:
            client.messages.create(to=number, from_=to,
                               body=target + 'is not a known contact')
            return HttpResponse('')
        convo, created = Conversation.objects.get_or_create(from_phone=number, to_phone=contacts[0].number,
                                                   user=user)
        if created:
            convo.expires_at = datetime.now() + timedelta(minutes=15)
            convo.save()
        client.messages.create(to=contacts[0].number, from_=to,
                                         body=message_body)
        return HttpResponse("")
    convos = Conversation.objects.filter(from_phone=number, user=user, expires_at__gte=datetime.now())
    if len(convos) == 0:
        client.messages.create(to=number, from_=to,
                               body='You have no open conversations and the message does not start with @<contact_name>')
        return HttpResponse("")
    if len(convos) > 1:
        client.messages.create(to=number, from_=to,
                               body='You have multiple open conversations and the message does not start with @<contact_name>')
        return HttpResponse("")
    client.messages.create(to=convos[0].to_number, from_=to, body=message_body)
    return HttpResponse("")
