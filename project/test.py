import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django.setup()

from etl.models import Subscription

print(Subscription.objects.all())

#sub1 = Subscription(plan="monthly")