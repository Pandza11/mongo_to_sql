from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.timezone import datetime

# Create your models here.


class Subscription(models.Model):
    """
    Represents a subscription.
    """
    plan = models.CharField(max_length=1024, blank=False)
    lastPayment = models.DateField(default=datetime.today)
    createdAt = models.DateField(default=datetime.today)
    paypalAgreementId = models.CharField(max_length=1024, blank=False)
    isSuspended = models.BooleanField(default=False)
    hosts = models.CharField(max_length=1024)
    memberLimit = models.IntegerField(default=1)
    period = models.CharField(max_length=1024, default="monthly")
    couponID = models.CharField(max_length=1024)

    def __str__(self):
        return self.couponID


class Account(models.Model):
    """
    Represents a registered user.
    """
    # what to do with index: { unique: true } in email?
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=1024, blank=False)
    createdAt = models.DateField(default=datetime.today)
    name = models.CharField(max_length=1024)
    # what to do with index: { unique: true } in key?
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(max_length=1024, default=datetime.today)
    # What should the default be?
    defaultTTL = models.IntegerField(default=None)
    googleProfile_id = models.CharField(max_length=1024)
    googleProfile_username = models.CharField(max_length=1024)
    googleProfile_displayname = models.CharField(max_length=1024)
    facebookProfile_id = models.CharField(max_length=1024)
    facebookProfile_username = models.CharField(max_length=1024)
    facebookProfile_displayname = models.CharField(max_length=1024)
    twitterProfile_id = models.CharField(max_length=1024)
    twitterProfile_username = models.CharField(max_length=1024)
    twitterProfile_displayname = models.CharField(max_length=1024)
    subscriptions = models.ForeignKey(Subscription)
    referral = models.CharField(max_length=1024)
    refSrc = models.CharField(max_length=1024)
    firstSeen = models.DateField()
    enableClassroom = models.BooleanField(default=False)
    memberOf = models.CharField(max_length=1024)
    isAffiliate = models.BooleanField()
    isAWWAdmin = models.BooleanField()
    accountType = models.CharField(max_length=1024, default='fun')
    enableNewsletter = models.BooleanField()
    lastLoginAt = models.DateField(default=datetime.date(2017, 1, 1))

    def __str__(self):
        return self.name
