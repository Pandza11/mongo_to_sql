import pymongo
import sqlite3

def change_keyname(oldkey,newkey):
    """Renames dictionary key"""
    if account.get(oldkey):
        account[newkey] = account.pop(oldkey)

def change_keyname_socialnetwork(socialnetwork):
    """Renames dictionary key embedded within a dictionary"""
    social_list = ["id", "username", "displayName"]
    if account.get(socialnetwork+"Profile"):
        for item in social_list:
            if account.get(socialnetwork+"Profile").get(item):
                account[socialnetwork+"_profile_"+item.lower()] = account.get(socialnetwork+"Profile").pop(item)
    account.pop(socialnetwork+"Profile", None)       

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

accounts_list = []
subscriptions_list = []

for account in db.accounts.find():
    for item in account["subscriptions"]:
        subscriptions_list.append(item)


for account in db.accounts.find():
    account.pop("_id", None) # Deleted according to instructions
    account.pop("__v", None) # Deleted according to instructions
    account.pop("password", None)  # Deleted according to instructions
    account.pop("isCommboxAdmin", None) # Deleted here because unimportant (appears twice in db)
    account.pop("googleId", None)   # Deleted here because it appears twice in the mongo database
    account.pop("facebookId", None) # Deleted here because it appears twice in the mongo database
    account.pop("twitterId", None)  # Deleted here because it appears twice in the mongo database
    account.pop("subscriptions", None) # Requires further work
    account.pop("enableNewsletter", None) # Function change_keyname doesn't work

    change_keyname("accountType","account_type")
    change_keyname("enableClassroom","enable_classroom")
    change_keyname("refSrc","ref_src")
    change_keyname("firstSeen","firstSeen")
    change_keyname("isAffiliate","is_affiliate")
    change_keyname("deletedAt","deleted_at")
    change_keyname("memberOf","member_of")
    change_keyname("defaultTTL","default_ttl")
    change_keyname("lastLoginAt","last_login_at")
    change_keyname("isAWWAdmin","is_aww_admin")
    change_keyname("createdAt","created_at")
    change_keyname_socialnetwork("google")
    change_keyname_socialnetwork("facebook")
    change_keyname_socialnetwork("twitter")

    accounts_list.append(account)


for value in accounts_list:
    conn = sqlite3.connect('/home/ivan/pandzic/myproject/db.sqlite3')
    cursor = conn.cursor()

    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))


    sql = 'INSERT INTO etl_account ({}) VALUES ({})'.format(columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
    conn.close()
