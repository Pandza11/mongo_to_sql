# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 10:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateField(default=datetime.datetime.today)),
                ('name', models.CharField(blank=True, max_length=1024, null=True)),
                ('key', models.CharField(blank=True, max_length=1024, null=True, unique=True)),
                ('date', models.DateField(default=datetime.datetime.today, max_length=1024)),
                ('default_ttl', models.IntegerField(blank=True, default=None, null=True)),
                ('google_profile_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('google_profile_username', models.CharField(blank=True, max_length=1024, null=True)),
                ('google_profile_displayname', models.CharField(blank=True, max_length=1024, null=True)),
                ('facebook_profile_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('facebook_profile_username', models.CharField(blank=True, max_length=1024, null=True)),
                ('facebook_profile_displayname', models.CharField(blank=True, max_length=1024, null=True)),
                ('twitter_profile_id', models.CharField(blank=True, max_length=1024, null=True)),
                ('twitter_profile_username', models.CharField(blank=True, max_length=1024, null=True)),
                ('twitter_profile_displayname', models.CharField(blank=True, max_length=1024, null=True)),
                ('referral', models.CharField(blank=True, max_length=1024, null=True)),
                ('ref_src', models.CharField(blank=True, max_length=1024, null=True)),
                ('first_seen', models.DateField(blank=True, null=True)),
                ('enable_classroom', models.NullBooleanField(default=False)),
                ('member_of', models.CharField(blank=True, max_length=1024, null=True)),
                ('is_affiliate', models.NullBooleanField()),
                ('is_www_admin', models.NullBooleanField()),
                ('account_type', models.CharField(blank=True, default='fun', max_length=1024, null=True)),
                ('enable_newsletter', models.NullBooleanField()),
                ('last_login_at', models.DateField(blank=True, default=None, null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=1024, null=True)),
                ('last_payment', models.DateField(default=datetime.datetime.today, null=True)),
                ('created_at', models.DateField(default=datetime.datetime.today, null=True)),
                ('paypal_agreement_id', models.CharField(max_length=1024, null=True)),
                ('is_suspended', models.BooleanField(default=False)),
                ('hosts', models.CharField(max_length=1024, null=True)),
                ('member_limit', models.IntegerField(default=1, null=True)),
                ('period', models.CharField(default='monthly', max_length=1024)),
                ('coupon_id', models.CharField(max_length=1024, null=True)),
                ('deleted_at', models.DateField(default=None, null=True)),
                ('account', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='etl.Account')),
            ],
        ),
    ]
