import pymongo
import sqlite3

def unicode_to_bool(s):
    if s == "True":
        return True
    else:
        return False


def change_keyname(oldkey,newkey):
    """Renames dictionary key"""
    if subscription.get(oldkey):
        subscription[newkey] = subscription.pop(oldkey)

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

subscriptions_list = []

for account in db.accounts.find():
    for item in account["subscriptions"]:
        subscriptions_list.append(item)

for subscription in subscriptions_list:
    if len(subscription) > 0:
        #subscription["created_at"] = subscription.pop("createdAt")
        #subscription["paypal_agreement_id"] = subscription.pop("paypalAgreementId")
        
        '''

        if subscription.get("lastPayment"):
            subscription["last_payment"] = subscription.pop("lastPayment")
        '''

        #change_keyname("memberLimit","member_limit")

        if subscription.get("couponId"):
            subscription["coupon_id"] = subscription.pop("couponId")
            subscription["coupon_id"] = subscription["coupon_id"].encode("utf-8")

        if subscription.get("plan"):
            subscription["plan"] = subscription["plan"].encode("utf-8")

        if subscription.get("period"):
            subscription["period"] = subscription["period"].encode("utf-8")

        #if subscription.get("hosts"):
        #    hosts = subscription["hosts"]
        #    x = ''.join(hosts).encode("utf-8")
        #    print type(x)
        #    subscription.pop("hosts", None)

        subscription.pop("lastPayment", None)
        subscription.pop("hosts", None)
        subscription.pop("createdAt", None)
        subscription.pop("paypalAgreementId", None)
        subscription.pop("isSuspended", None)
        subscription.pop("memberLimit", None)
        subscription.pop("_id", None)

print(subscriptions_list[0])


for value in subscriptions_list:

    conn = sqlite3.connect('/home/ivan/pandzic/myproject/db.sqlite3')
    cursor = conn.cursor()

    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))

    sql = 'INSERT INTO etl_subscription ({}) VALUES ({})'.format(columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
    conn.close()
