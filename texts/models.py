from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    number = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey(User)

class TwilioNumber(models.Model):
    number = models.CharField(max_length=30, null=False, unique=True)
    user = models.ForeignKey(User)

class Conversation(models.Model):
    from_phone = models.CharField(max_length=30)
    to_phone = models.CharField(max_length=30)
    expires_at = models.DateTimeField()
    user = models.ForeignKey(User)