from django.contrib import admin

from texts.models import Contact, Conversation, TwilioNumber

admin.site.register(Contact)
admin.site.register(Conversation)
admin.site.register(TwilioNumber)