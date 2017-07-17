import pymongo
import sqlite3

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

accounts_list = []
subscriptions_list = []

for account in db.accounts.find():
    try:
        for n in range(1):
            subscriptions_n = account["subscriptions"][n]
            #subscriptions_n["last_payment"] = subscriptions_n.pop("lastPayment")
            #subscriptions_n["created_at"] = subscriptions_n.pop("createdAt")
            #subscriptions_n["paypal_agreement_id"] = subscriptions_n.pop("paypalAgreementId")
            #subscriptions_n["is_suspended"] = subscriptions_n.pop("isSuspended")
            #subscriptions_n["member_limit"] = subscriptions_n.pop("memberLimit")
            subscriptions_n["coupon_id"] = subscriptions_n.pop("couponId")
            subscriptions_n.pop("_id", None)
            subscriptions_n.pop("hosts", None)
            subscriptions_n.pop("coupon_id", None)
            subscriptions_n.pop("period", None)
            subscriptions_n.pop("lastPayment", None)
            subscriptions_n.pop("createdAt", None)
            subscriptions_n.pop("paypalAgreementId", None)
            subscriptions_n.pop("isSuspended", None)
            subscriptions_n.pop("memberLimit", None)
            #subscriptions_n.pop("_id", None)
            #subscriptions_n.pop("_id", None)
            #subscriptions_n.pop("_id", None)
            subscriptions_list.append(subscriptions_n)
    except (IndexError, KeyError):
        continue

print(subscriptions_list[0].keys())


for value in subscriptions_list:
    conn = sqlite3.connect('/home/ivan/pandzic/myproject/db.sqlite3')
    cursor = conn.cursor()

    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))

    sql = 'INSERT INTO etl_subscription ({}) VALUES ({})'.format(columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
    conn.close()
