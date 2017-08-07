import os
import django
import pymongo
from django.db import IntegrityError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from etl.models import Account, Subscription

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp
account_list, subscriptions_list = [], []
counter = 0


def create_social_kv_pairs(socialnetwork):
    """
    Creates three key value pairs out of social network components
    embedded in a dictionary within the db.accounts collection/dictionary.
    """
    social_componets = ["id", "username", "displayName"]
    for component in social_componets:
        try:
            account[socialnetwork+"_profile_"+component.lower()] = account[
                socialnetwork+"Profile"][component]
        except KeyError:
            pass


for account in db.accounts.find():
    #counter += 1
    #print counter
    for subscription in account["subscriptions"]:
        #subscription["account_id"] = counter
        subscriptions_list.append(subscription)

    social_networks = ["google", "facebook", "twitter"]
    for network in social_networks:
        create_social_kv_pairs(network)
    account_list.append(account)


for subscription in subscriptions_list:
    try:
        hosts_list = filter(None, subscription["hosts"])
        if len(hosts_list) == 1:
            hosts_str = ''.join(hosts_list)
        elif len(hosts_list) > 1:
            hosts_str = ', '.join(hosts_list)
        subscription["hosts"] = hosts_str
    except KeyError:
        pass

missing_keys_accounts = [
    "name", "key", "date", "referral", "email", "accountType",
    "enableClassroom", "refSrc", "firstSeen", "isAffiliate",
    "deletedAt", "memberOf", "defaultTTL", "lastLoginAt",
    "isAWWAdmin", "createdAt", "enableNewsletter", "google_profile_id",
    "google_profile_username", "google_profile_displayname",
    "facebook_profile_id", "facebook_profile_username",
    "facebook_profile_displayname", "twitter_profile_id",
    "twitter_profile_username", "twitter_profile_displayname"
    ]

missing_keys_subscriptions = [
    "lastPayment", "isSuspended", "hosts",
    "memberLimit", "period", "couponId"
    ]

for account_key in missing_keys_accounts:
    for account in account_list:
        try:
            value = account[account_key]
        except KeyError:
            account[account_key] = None

for subscription_key in missing_keys_subscriptions:
    for subscription in subscriptions_list:
        try:
            value = subscription[subscription_key]
        except KeyError:
            subscription[subscription_key] = None

for subscription in subscriptions_list:
    subscription_object = Subscription(
        plan=subscription["plan"], created_at=subscription["createdAt"],
        paypal_agreement_id=subscription["paypalAgreementId"],
        last_payment=subscription["lastPayment"],
        is_suspended=subscription["isSuspended"],
        hosts=subscription["hosts"], member_limit=subscription["memberLimit"],
        period=subscription["period"], coupon_id=subscription["couponId"],
        #account_id=subscription["account_id"]
        )
    subscription_object.save()


except IntegrityError as e: 
    if 'unique constraint' in e.message: # or e.args[0] from Django 1.10
        #do something

        for account in account_list:
            account_object = Account(
                email=account["email"], created_at=account["createdAt"],
                name=account["name"], key=account["key"], date=account["date"],
                default_ttl=account["defaultTTL"],
                google_profile_id=account["google_profile_id"],
                google_profile_username=account["google_profile_username"],
                google_profile_displayname=account["google_profile_displayname"],
                facebook_profile_id=account["facebook_profile_id"],
                facebook_profile_username=account["facebook_profile_username"],
                facebook_profile_displayname=account["facebook_profile_displayname"],
                twitter_profile_id=account["twitter_profile_id"],
                twitter_profile_username=account["twitter_profile_username"],
                twitter_profile_displayname=account["twitter_profile_displayname"],
                referral=account["referral"], ref_src=account["refSrc"],
                first_seen=account["firstSeen"],
                enable_classroom=account["enableClassroom"],
                member_of=account["memberOf"], is_affiliate=account["isAffiliate"],
                is_aww_admin=account["isAWWAdmin"],
                account_type=account["accountType"],
                enable_newsletter=account["enableNewsletter"],
                last_login_at=account["lastLoginAt"]
                )
            account_object.save()
