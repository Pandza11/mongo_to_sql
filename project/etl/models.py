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
    name = models.CharField(max_length=1024, null=True, blank=True)
    key = models.CharField(max_length=1024, unique=True, null=True, blank=True)
    date = models.DateField(max_length=1024, default=datetime.today)
    default_ttl = models.IntegerField(default=None, unique=True, null=True, blank=True)
    google_profile_id = models.CharField(max_length=1024, null=True, blank=True)
    google_profile_username = models.CharField(max_length=1024, null=True, blank=True)
    google_profile_displayname = models.CharField(max_length=1024, null=True, blank=True)
    facebook_profile_id = models.CharField(max_length=1024, null=True, blank=True)
    facebook_profile_username = models.CharField(max_length=1024, null=True, blank=True)
    facebook_profile_displayname = models.CharField(max_length=1024, null=True, blank=True)
    twitter_profile_id = models.CharField(max_length=1024, null=True, blank=True)
    twitter_profile_username = models.CharField(max_length=1024, null=True, blank=True)
    twitter_profile_displayname = models.CharField(max_length=1024, null=True, blank=True)
    referral = models.CharField(max_length=1024, null=True, blank=True)
    ref_src = models.CharField(max_length=1024, null=True, blank=True)
    first_seen = models.DateField(null=True, blank=True)
    enable_classroom = models.NullBooleanField(default=False, null=True, blank=True)
    member_of = models.CharField(max_length=1024, null=True, blank=True)
    is_affiliate = models.NullBooleanField(null=True, blank=True)
    is_aww_admin = models.NullBooleanField(null=True, blank=True)
    account_type = models.CharField(max_length=1024, default='fun', null=True, blank=True)
    enable_newsletter = models.NullBooleanField(null=True, blank=True)
    last_login_at = models.DateField(default=None, null=True, blank=True)
    deleted_at = models.DateField(default=None, null=True, blank=True)

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
