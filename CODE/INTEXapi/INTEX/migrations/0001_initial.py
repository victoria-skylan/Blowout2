# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='campaigns',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('url', models.TextField()),
                ('auto_fb_post_mode', models.TextField()),
                ('collected_date', models.TextField()),
                ('category_id', models.IntegerField()),
                ('category', models.TextField()),
                ('currencycode', models.TextField()),
                ('current_amount', models.IntegerField()),
                ('goal', models.IntegerField()),
                ('donators', models.IntegerField()),
                ('days_active', models.IntegerField()),
                ('days_created', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('has_beneficiary', models.BooleanField()),
                ('media_type', models.IntegerField()),
                ('project_type', models.IntegerField()),
                ('turn_off_donations', models.BooleanField()),
                ('user_id', models.IntegerField()),
                ('user_first_name', models.TextField()),
                ('user_last_name', models.TextField()),
                ('user_facebook_id', models.TextField()),
                ('user_profile_url', models.TextField()),
                ('visible_in_search', models.BooleanField()),
                ('status', models.IntegerField()),
                ('deactivated', models.BooleanField()),
                ('state', models.TextField()),
                ('is_launched', models.BooleanField()),
                ('campaign_image_url', models.TextField()),
                ('created_at', models.TextField()),
                ('launch_date', models.TextField()),
                ('campaign_hearts', models.IntegerField()),
                ('social_share_total', models.IntegerField()),
                ('social_share_last_update', models.TextField()),
                ('location_city', models.TextField()),
                ('location_country', models.TextField()),
                ('location_zip', models.TextField()),
                ('is_charity', models.BooleanField()),
                ('charity_valid', models.BooleanField()),
                ('charity_npo_id', models.TextField()),
                ('charity_name', models.TextField()),
                ('velocity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
                ('admin', models.BooleanField()),
            ],
        ),
    ]
