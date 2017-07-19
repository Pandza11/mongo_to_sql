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


client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

subscriptions_list = []

for account in db.accounts.find():
    for item in account["subscriptions"]:
        subscriptions_list.append(item)

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

print(subscriptions_list[0])


for value in subscriptions_list:

    conn = sqlite3.connect(
        '/home/dobar-kod/pandzic/project-aww/aww-etl/project/db.sqlite3')
    cursor = conn.cursor()

    columns = ', '.join(value.keys())
    placeholders = ', '.join('?' * len(value))

    sql = 'INSERT INTO etl_subscription ({}) VALUES ({})'.format(
        columns, placeholders)
    cursor.execute(sql, tuple(value.values()))

    conn.commit()
    conn.close()
