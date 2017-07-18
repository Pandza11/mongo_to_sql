import pymongo
import sqlite3

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

accounts_list = []
subscriptions_list = []

for account in db.accounts.find():
    account.pop("password", None)
    account["created_at"] = account.pop("createdAt")
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
        account["is_www_admin"] = account.pop("isAWWAdmin")
    #if account.get("facebookId"):
    #    account["facebook_id"] = account.pop("facebookId")
    account.pop("isCommboxAdmin", None)
    account.pop("googleProfile", None)
    account.pop("googleId", None)
    account.pop("facebookProfile", None)
    account.pop("facebookId", None)
    account.pop("twitterProfile", None)
    account.pop("twitterId", None)
    account.pop("subscriptions", None)
    account.pop("_id", None)
    account.pop("__v", None)
    account.pop("_id", None)
    accounts_list.append(account)

print(accounts_list[0].keys())

for value in accounts_list:
    conn = sqlite3.connect('/home/ivan/pandzic/myproject/db.sqlite3')
    cursor = conn.cursor()

    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))


    sql = 'INSERT INTO etl_account ({}) VALUES ({})'.format(columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
    conn.close()
