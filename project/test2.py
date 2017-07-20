import os
import django
import pymongo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from etl.models import Account

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

account_list = []


def correct_typo(oldkey, newkey):
    """
    Renames dictionary key in order to correct typo
    """
    try:
        account[newkey] = account.pop(oldkey)
    except KeyError:
        pass


def create_social_kv_pairs(socialnetwork):
    """
    Creates three key value pairs out of social network items
    embedded in a dictionary within the db.accounts collection/dictionary.
    """
    social_list = ["id", "username", "displayName"]

    for item in social_list:
        try:
            account[socialnetwork+"_profile_"+item.lower()] = account[
                socialnetwork+"Profile"][item]
        except KeyError:
            pass


for account in db.accounts.find():
    correct_typo("subcriprions", "subscriptions")
    correct_typo("subcriptions", "subcriptions")

    social_networks = ["google", "facebook", "twitter"]
    for item in social_networks:
        create_social_kv_pairs(item)

    account_list.append(account)

missing_key_accounts = [
    "name", "key", "date", "referral", "email", "accountType",
    "enableClassroom", "refSrc", "firstSeen", "isAffiliate",
    "deletedAt", "memberOf", "defaultTTL", "lastLoginAt",
    "isAWWAdmin", "createdAt", "enableNewsletter", "google_profile_id",
    "google_profile_username", "google_profile_displayname",
    "facebook_profile_id", "facebook_profile_username",
    "facebook_profile_displayname", "twitter_profile_id",
    "twitter_profile_username", "twitter_profile_displayname"]

for key in missing_key_accounts:
    for account in account_list:
        try:
            value = account[key]
        except KeyError:
            account[key] = None

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
        member_of=account["memberOf"],
        is_affiliate=account["isAffiliate"],
        is_aww_admin=account["isAWWAdmin"],
        account_type=account["accountType"],
        enable_newsletter=account["enableNewsletter"],
        last_login_at=account["lastLoginAt"])
    account_object.save()
