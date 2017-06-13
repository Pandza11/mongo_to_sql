from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import datetime

# Create your models here.

class Account(models.Model):
    """
    Represents a registered user.
    """
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=1024, blank=False)
    createdAt = models.DateField(null=True, blank=True, default=None)
    name = models.CharField(max_length=1024)
    key = models.CharField(max_length=1024, default='uuid') # What to do with UUID?
    date = models.DateField(max_length=1024, default=datetime.today)
    defaultTTL = models.IntegerField(max_length=1024)
    googleId = models.CharField(max_length=1024)
    facebookId = models.CharField(max_length=1024)
    twitterId = models.CharField(max_length=1024)
    googleProfile_id = models.CharField(max_length=1024)
    googleProfile_username = models.CharField(max_length=1024)
    googleProfile_displayname = models.CharField(max_length=1024)
    facebookProfile_id = models.CharField(max_length=1024)
    facebookProfile_username = models.CharField(max_length=1024)
    facebookProfile_displayname = models.CharField(max_length=1024)
    twitterProfile_id = models.CharField(max_length=1024)
    twitterProfile_username = models.CharField(max_length=1024)
    twitterProfile_displayname = models.CharField(max_length=1024)
    subscriptions = models.CharField(max_length=1024)
    referral = models.CharField(max_length=1024)
    refSrc = models.CharField(max_length=1024)
    firstSeen = models.DateField(max_length=1024)
    enableClassroom = models.BooleanField(default=False)
    memberOf = models.CharField(max_length=1024)
    isAffiliate = models.BooleanField(default=False)
    isAWWAdmin = models.BooleanField(default=False)
    accountType = models.CharField(max_length=1024, default='fun')
    enableNewsletter = models.BooleanField(default=False)
    lastLoginAt = models.DateField(max_length=1024)

    def __str__(self):
        return self.name

class Subscription(models.Model):
    """
    Represents a subscription.
    """
    plan = models.CharField(max_length=1024, blank=False)
    lastPayment = models.DateField(max_length=1024, default=datetime.today)
    createdAt = models.DateField(max_length=1024, default=datetime.today)
    paypalAgreementId = models.CharField(max_length=1024, blank=False)
    isSuspended = models.BooleanField(default=False)
    hosts = models.CharField(max_length=1024)
    memberLimit = models.IntegerField(max_length=1024, default=1)
    period = models.CharField(max_length=1024, default="monthly")
    couponID = models.CharField(max_length=1024)

    def __str__(self):
        return self.couponID
