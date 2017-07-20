import os
import django
import pymongo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from etl.models import Subscription


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

missing_keys = ["last_payment", "is_suspended", "hosts",
                "member_limit", "period", "coupon_id"]

for key in missing_keys:
    for item in subscriptions_list:
        try:
            value = item[key]
        except KeyError:
            item[key] = None


for item in subscriptions_list:
    sub = Subscription(plan=item["plan"], created_at=item["created_at"],
                       paypal_agreement_id=item["paypal_agreement_id"],
                       last_payment=item["last_payment"],
                       is_suspended=item["is_suspended"],
                       hosts=item["hosts"], member_limit=item["member_limit"],
                       period=item["period"], coupon_id=item["coupon_id"])
    sub.save()


#print(Subscription.objects.all())
