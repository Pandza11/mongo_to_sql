import pymongo
import sqlite3

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

accounts_list = []
subscriptions_list = []

for account in db.accounts.find():
    for item in account["subscriptions"]:
        subscriptions_list.append(item)


for account in db.accounts.find():
    account.pop("_id", None)
    account.pop("__v", None)
    account.pop("password", None)
    account.pop("isCommboxAdmin", None)
    account.pop("googleId", None)
    account.pop("facebookId", None)
    account.pop("twitterId", None)
    account.pop("subscriptions", None)

    account["created_at"] = account.pop("createdAt")
    if account.get("googleProfile"):
        if account.get("googleProfile").get("id"):
            account["google_profile_id"] = account.get("googleProfile").pop("id")
        if account.get("googleProfile").get("id"):
            account["google_profile_username"] = account.get("googleProfile").pop("username")
        if account.get("googleProfile").get("id"):
            account["google_profile_displayname"] = account.get("googleProfile").pop("displayName")
        account.pop("googleProfile", None)

    if account.get("facebookProfile"):
        if account.get("facebookProfile").get("id"):
            account["facebook_profile_id"] = account.get("facebookProfile").pop("id")
        if account.get("facebookProfile").get("id"):
            account["facebook_profile_username"] = account.get("facebookProfile").pop("username")
        if account.get("facebookProfile").get("id"):
            account["facebook_profile_displayname"] = account.get("facebookProfile").pop("displayName")
        account.pop("facebookProfile", None)

    if account.get("twitterProfile"):
        if account.get("twitterProfile").get("id"):
            account["twitter_profile_id"] = account.get("twitterProfile").pop("id")
        if account.get("twitterProfile").get("id"):
            account["twitter_profile_username"] = account.get("twitterProfile").pop("username")
        if account.get("twitterProfile").get("id"):
            account["twitter_profile_displayname"] = account.get("twitterProfile").pop("displayName")
        account.pop("twitterProfile", None)

    #def change_name(oldkey,newkey):
    #    "Renames key of dictionary"

    if account.get("accountType"):
        account["account_type"] = account.pop("accountType")

    if account.get("enableClassroom"):
        account["enable_classroom"] = account.pop("enableClassroom")

    if account.get("refSrc"):
        account["ref_src"] = account.pop("refSrc")

    if account.get("firstSeen"):
        account["first_seen"] = account.pop("firstSeen")

    if account.get("isAffiliate"):
        account["is_affiliate"] = account.pop("isAffiliate")

    if account.get("deletedAt"):
        account["deletedAt"] = account.pop("deletedAt")

    if account.get("memberOf"):
        account["member_of"] = account.pop("memberOf") # radi

    if account.get("defaultTTL"):
        account["default_ttl"] = account.pop("defaultTTL")

    if account.get("lastLoginAt"):
        account["last_login_at"] = account.pop("lastLoginAt")

    if account.get("enableNewsletter"):
        account["enable_newsletter"] = account.pop("enableNewsletter")

    if account.get("isAWWAdmin"):
        account["is_aww_admin"] = account.pop("isAWWAdmin")

    accounts_list.append(account)

print(accounts_list[0])



for value in accounts_list:
    conn = sqlite3.connect('/home/ivan/pandzic/myproject/db.sqlite3')
    cursor = conn.cursor()

    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))


    sql = 'INSERT INTO etl_account ({}) VALUES ({})'.format(columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
    conn.close()
