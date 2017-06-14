from django.contrib import admin

from .models import Subscription, Account


class SubscriptionInline(admin.StackedInline):
    model = Subscription


class AccountAdmin(admin.ModelAdmin):
    inlines = [SubscriptionInline]


admin.site.register(Account, AccountAdmin)
