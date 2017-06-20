from __future__ import unicode_literals

from django.db import models
from django.utils.timezone import datetime

# Create your models here.


class Account(models.Model):
    """
    Represents a registered User.
    """
    email = models.EmailField(max_length=254, blank=False, unique=True)
    created_at = models.DateField(default=datetime.today)
    name = models.CharField(max_length=1024)
    key = models.CharField(max_length=1024, unique=True)
    date = models.DateField(max_length=1024, default=datetime.today)
    default_ttl = models.IntegerField(default=None, unique=True)
    google_profile_id = models.CharField(max_length=1024)
    google_profile_username = models.CharField(max_length=1024)
    google_profile_displayname = models.CharField(max_length=1024)
    facebook_profile_id = models.CharField(max_length=1024)
    facebook_profile_username = models.CharField(max_length=1024)
    facebook_profile_displayname = models.CharField(max_length=1024)
    twitter_profile_id = models.CharField(max_length=1024)
    twitter_profile_username = models.CharField(max_length=1024)
    twitter_profile_displayname = models.CharField(max_length=1024)
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
    deleted_at = models.DateField(default=None)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    """
    Represents a subscription by a User.
    """
    plan = models.CharField(max_length=1024, blank=False)
    last_payment = models.DateField(default=datetime.today)
    created_at = models.DateField(default=datetime.today)
    paypal_agreement_id = models.CharField(max_length=1024, blank=False)
    is_suspended = models.BooleanField(default=False)
    member_limit = models.IntegerField(default=1)
    period = models.CharField(max_length=1024, default="monthly")
    coupon_id = models.CharField(max_length=1024)
    account = models.ForeignKey(Account, default=None)
    deleted_at = models.DateField(default=None)

    def __str__(self):
        return self.coupon_id
