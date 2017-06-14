from django.contrib import admin

# Register your models here.

from .models import Subscription, Account
# Register your models here.


class SubscriptionInline(admin.StackedInline):
    model = Subscription


class AccountAdmin(admin.ModelAdmin):
    inlines = [SubscriptionInline]


admin.site.register(Account, AccountAdmin)
