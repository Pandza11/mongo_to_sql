import os
import datetime
import django
import pymongo

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from etl.models import Account, Subscription

client = pymongo.MongoClient("localhost", 27017)
db = client.awwapp
account_list, subscriptions_list = [], []


for account in db.accounts.find():
    for subscription in account["subscriptions"]:
        subscriptions_list.append(subscription)


for subscription in subscriptions_list:
    try:
        hosts_list = filter(None, subscription["hosts"])
        if len(hosts_list) == 1:
            hosts_str = ''.join(hosts_list)
        elif len(hosts_list) > 1:
            hosts_str = ', '.join(hosts_list)
        subscription["hosts"] = hosts_str
    except KeyError:
        pass

del account_list[11]
del account_list[11]

email_list_old = []
email_list_new = []


for obj in Account.objects.all():
    email_list_old.append(obj.email)

for account in account_list:
    email_list_new.append(account["email"])

now = datetime.datetime.now()
date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)

for email in email_list_old:
    if email not in email_list_new:
        obj = Account.objects.get(email=email)
        obj.deleted_at = date
        obj.save()
