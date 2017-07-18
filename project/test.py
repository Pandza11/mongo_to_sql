import pymongo
import sqlite3


def change_keyname(oldkey, newkey):
    """
    Renames dictionary key
    """
    try:
        account[newkey] = account.pop(oldkey)
    except KeyError:
        pass


def change_keyname_socialnetwork(socialnetwork):
    """
    Renames dictionary key embedded within another dictionary
    """
    social_list = ["id", "username", "displayName"]
    if account.get(socialnetwork+"Profile"):
        for item in social_list:
            if account.get(socialnetwork+"Profile").get(item):
                account[socialnetwork+"_profile_"+item.lower()] = account.get(
                    socialnetwork+"Profile").pop(item)
    account.pop(socialnetwork+"Profile", None)

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

accounts_list = []
subscriptions_list = []

for account in db.accounts.find():
    for item in account["subscriptions"]:
        subscriptions_list.append(item)


for account in db.accounts.find():
    deletion_list = ["_id", "__v", "password", "isCommboxAdmin", "googleId",
                     "facebookId", "twitterId", "subscriptions",
                     "enableNewsletter"]
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
                           ["createdAt", "created_at"]]
    for item in change_keyname_list:
        change_keyname(item[0], item[1])

    change_keyname_socialnetwork_list = ["google", "facebook", "twitter"]
    for item in deletion_list:
        change_keyname_socialnetwork(item)

    accounts_list.append(account)


for value in accounts_list:
    conn = sqlite3.connect(
        '/home/ivan/projects/project-aww/aww-etl/project/db.sqlite3')
    cursor = conn.cursor()

    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))

    sql = 'INSERT INTO etl_account ({}) VALUES ({})'.format(
        columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
    conn.close()
