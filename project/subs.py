import pymongo
import sqlite3


def change_keyname(oldkey, newkey):
    """
    Renames dictionary key
    """

    try:
        subscription[newkey] = subscription.pop(oldkey)
    except KeyError:
        pass

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

subscriptions_list = []

for account in db.accounts.find():
    for item in account["subscriptions"]:
        subscriptions_list.append(item)

for subscription in subscriptions_list:
    if len(subscription) > 0:
        subscription.pop("_id", None)

        change_keyname("memberLimit", "member_limit")
        change_keyname("isSuspended", "is_suspended")
        change_keyname("paypalAgreementId", "paypal_agreement_id")
        change_keyname("lastPayment", "last_payment")
        change_keyname("createdAt", "created_at")
        change_keyname("couponId", "coupon_id")
        change_keyname("plan", "plan")
        change_keyname("period", "period")

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

print(subscriptions_list[0])


for value in subscriptions_list:

    conn = sqlite3.connect(
        '/home/ivan/projects/project-aww/aww-etl/project/db.sqlite3')
    cursor = conn.cursor()

    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))

    sql = 'INSERT INTO etl_subscription ({}) VALUES ({})'.format(
        columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
    conn.close()
