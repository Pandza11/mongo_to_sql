import pymongo
import sqlite3


def change_keyname(oldkey, newkey, collection):
    """
    Renames dictionary key of a collection
    """
    try:
        collection[newkey] = collection.pop(oldkey)
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

db_path_sqlite = '/home/ivan/projects/project-aww/aww-etl/project/db.sqlite3'

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

accounts_list = []
subscriptions_list = []


for account in db.accounts.find():
    for item in account["subscriptions"]:
        subscriptions_list.append(item)
    deletion_list = ["_id", "__v", "password", "isCommboxAdmin",
                     "lastModified", "googleId", "facebookId", "twitterId",
                     "subscriptions"]
    for item in deletion_list:
        account.pop(item, None)

    change_keyname_list = [["accountType", "account_type"],
                           ["enableClassroom", "enable_classroom"],
                           ["refSrc", "ref_src"],
                           ["firstSeen", "firstSeen"],
                           ["isAffiliate", "is_affiliate"],
                           ["deletedAt", "deleted_at"],
                           ["memberOf", "member_of"],
                           ["defaultTTL", "default_ttl"],
                           ["lastLoginAt", "last_login_at"],
                           ["isAWWAdmin", "is_aww_admin"],
                           ["createdAt", "created_at"],
                           ["enableNewsletter", "enable_newsletter"]]
    for item in change_keyname_list:
        change_keyname(item[0], item[1], account)

    change_keyname_socialnetwork_list = ["google", "facebook", "twitter"]
    for item in change_keyname_socialnetwork_list:
        change_keyname_socialnetwork(item)

    accounts_list.append(account)

for value in accounts_list:
    conn = sqlite3.connect(db_path_sqlite)
    cursor = conn.cursor()
    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))
    sql = 'INSERT INTO etl_account ({}) VALUES ({})'.format(
        columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
conn.close()


for subscription in subscriptions_list:
    if len(subscription) > 0:
        subscription.pop("_id", None)

        change_keyname_list = [["memberLimit", "member_limit"],
                               ["isSuspended", "is_suspended"],
                               ["paypalAgreementId", "paypal_agreement_id"],
                               ["lastPayment", "last_payment"],
                               ["createdAt", "created_at"],
                               ["couponId", "coupon_id"],
                               ["plan", "plan"],
                               ["period", "period"]]

        for item in change_keyname_list:
            change_keyname(item[0], item[1], subscription)

        try:
            hosts_list = subscription["hosts"]
            if len(hosts_list) == 0:
                subscription.pop("hosts", None)
            elif len(hosts_list) == 1:
                hosts_str = hosts_list[0].encode("utf-8")
            elif len(hosts_list) > 1 and len(hosts_list[0]) > 0:
                hosts_str = ', '.join(hosts_list)
            subscription["hosts"] = hosts_str
        except KeyError:
            pass


for value in subscriptions_list:
    conn = sqlite3.connect(db_path_sqlite)
    cursor = conn.cursor()
    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))
    sql = 'INSERT INTO etl_subscription ({}) VALUES ({})'.format(
        columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
conn.close()
