import os
import django
import pymongo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from etl.models import Account

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

accounts_list = []

def change_keyname_typo(oldkey, newkey):
    """
    Renames dictionary key of a collection when typo
    """
    try:
        account[newkey] = account.pop(oldkey)
    except KeyError:
        pass


def change_keyname_socialnetwork(socialnetwork):
    """
    Renames dictionary key embedded within another dictionary (the collection)
    """
    social_list = ["id", "username", "displayName"]
    if account.get(socialnetwork+"Profile"):
        for item in social_list:
            if account.get(socialnetwork+"Profile").get(item):
                account[socialnetwork+"_profile_"+item.lower()] = account.get(
                    socialnetwork+"Profile").pop(item)
    account.pop(socialnetwork+"Profile", None)


for account in db.accounts.find():
    change_keyname_typo("subcriprions", "subscriptions")
    change_keyname_typo("subcriptions", "subcriptions")

    social_networks = ["google", "facebook", "twitter"]
    for item in social_networks:
        change_keyname_socialnetwork(item)

    accounts_list.append(account)

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
    for item in accounts_list:
        try:
            value = item[key]
        except KeyError:
            item[key] = None

for item in accounts_list:
    account = Account(
        email=item["email"], created_at=item["createdAt"],
        name=item["name"], key=item["key"], date=item["date"],
        default_ttl=item["defaultTTL"], google_profile_id=item["google_profile_id"],
        google_profile_username=item["google_profile_username"],
        google_profile_displayname=item["google_profile_displayname"],
        facebook_profile_id=item["facebook_profile_id"],
        facebook_profile_username=item["facebook_profile_username"],
        facebook_profile_displayname=item["facebook_profile_displayname"],
        twitter_profile_id=item["twitter_profile_id"],
        twitter_profile_username=item["twitter_profile_username"],
        twitter_profile_displayname=item["twitter_profile_displayname"],
        referral=item["referral"], ref_src=item["refSrc"], first_seen=item["firstSeen"],
        enable_classroom=item["enableClassroom"], member_of=item["memberOf"],
        is_affiliate=item["isAffiliate"], is_aww_admin=item["isAWWAdmin"],
        account_type=item["accountType"],
        enable_newsletter=item["enableNewsletter"],
        last_login_at=item["lastLoginAt"])
    account.save()
