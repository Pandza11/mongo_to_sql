from __future__ import unicode_literals
import uuid

from django.db import models
from django.utils.timezone import datetime

# Create your models here.


class Subscription(models.Model):
    """
    Represents a subscription by a User.
    """
    plan = models.CharField(max_length=1024, blank=False)
    last_payment = models.DateField(default=datetime.today)
    created_at = models.DateField(default=datetime.today)
    paypal_agreement_id = models.CharField(max_length=1024, blank=False)
    is_suspended = models.BooleanField(default=False)
    hosts = models.CharField(max_length=1024)
    member_limit = models.IntegerField(default=1)
    period = models.CharField(max_length=1024, default="monthly")
    coupon_iD = models.CharField(max_length=1024)

    def __str__(self):
        return self.couponID


class Account(models.Model):
    """
    Represents a registered User.
    """
    # what to do with index: { unique: true } in email?
    email = models.EmailField(max_length=254, blank=False)
    password = models.CharField(max_length=1024, blank=False)
    created_at = models.DateField(default=datetime.today)
    name = models.CharField(max_length=1024)
    # what to do with index: { unique: true } in key?
    key = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(max_length=1024, default=datetime.today)
    # What should the default be?
    default_ttl = models.IntegerField(default=None)
    google_profile_id = models.CharField(max_length=1024)
    google_profile_username = models.CharField(max_length=1024)
    google_profile_displayname = models.CharField(max_length=1024)
    facebook_profile_id = models.CharField(max_length=1024)
    facebook_profile_username = models.CharField(max_length=1024)
    facebook_profile_displayname = models.CharField(max_length=1024)
    twitter_profile_id = models.CharField(max_length=1024)
    twitter_profile_username = models.CharField(max_length=1024)
    twitter_profile_displayname = models.CharField(max_length=1024)
    subscriptions = models.ForeignKey(Subscription)
    referral = models.CharField(max_length=1024)
    ref_src = models.CharField(max_length=1024)
    first_seen = models.DateField()
    enable_classroom = models.BooleanField(default=False)
    member_of = models.CharField(max_length=1024)
    is_affiliate = models.BooleanField()
    is_aww_admin = models.BooleanField()
    account_type = models.CharField(max_length=1024, default='fun')
    enable_newsletter = models.BooleanField()
    last_login_at = models.DateField(default=None)

    def __str__(self):
        return self.name
