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
    #account["ref_src"] = account.pop("refSrc")
    #account["first_seen"] = account.pop("firstSeen")
    #account["is_affiliate"] = account.pop("isAffiliate")
    #account["enable_newsletter"] = account.pop("enableNewsletter")
    #account["last_login_at"] = account.pop("lastLoginAt")
    #account["deleted_at"] = account.pop("deletedAt")
    #account["member_of"] = account.pop("memberOf")
    #account["google_id"] = account.pop("googleId")
    #account["facebook_id"] = account.pop("facebookId")
    #account["twitter_id"] = account.pop("twitterId")
    account.pop("isCommboxAdmin", None)
    account.pop("refSrc", None)
    account.pop("firstSeen", None)
    account.pop("isAffiliate", None)
    account.pop("deletedAt", None)
    account.pop("memberOf", None)
    account.pop("googleId", None)
    account.pop("facebookId", None)
    account.pop("twitterId", None)
    account.pop("twitterProfile", None)
    account.pop("subscriptions", None)
    account.pop("_id", None)
    account.pop("__v", None)
    account.pop("facebookProfile", None)
    account.pop("googleProfile", None)
    account.pop("defaultTTL", None)
    account.pop("lastLoginAt", None)
    account.pop("enableNewsletter", None)
    account.pop("_id", None)
    account.pop("key", None)
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
