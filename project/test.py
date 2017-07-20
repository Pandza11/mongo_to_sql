import os
import django
import pymongo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from etl.models import Subscription


client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp

subscriptions_list = []

for account in db.accounts.find():
    for item in account["subscriptions"]:
        subscriptions_list.append(item)

missing_keys = ["lastPayment", "isSuspended", "hosts",
                "memberLimit", "period", "couponId"]

for key in missing_keys:
    for item in subscriptions_list:
        try:
            value = item[key]
        except KeyError:
            item[key] = None

'''
for item in subscriptions_list:
    sub = Subscription(plan=item["plan"], created_at=item["createdAt"],
                       paypal_agreement_id=item["paypalAgreementId"],
                       last_payment=item["lastPayment"],
                       is_suspended=item["isSuspended"],
                       hosts=item["hosts"], member_limit=item["memberLimit"],
                       period=item["period"], coupon_id=item["couponId"])
    sub.save()
'''