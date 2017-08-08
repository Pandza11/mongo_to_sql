import os
import django
import pymongo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from etl.models import Account, Subscription

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp
account_list, subscriptions_list = [], []
counter = 0


for account in db.accounts.find():
    print(account["email"])
    for subscription in account["subscriptions"]:
        subscription["email"] = account["email"]
        print(subscription["email"])
