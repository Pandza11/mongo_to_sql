from django.contrib import admin

# Register your models here.

from .models import Subscription, Account
# Register your models here.

admin.site.register(Subscription)
admin.site.register(Account)
