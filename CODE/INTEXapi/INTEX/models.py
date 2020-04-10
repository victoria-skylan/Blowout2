# -*- coding= utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    email = models.EmailField()
    password = models.TextField()


class campaigns(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.TextField(null=True)
    auto_fb_post_mode = models.TextField(null=True)
    collected_date = models.TextField(null=True)
    category_id = models.IntegerField(null=True)
    category= models.TextField(null=True)
    currencycode = models.TextField(null=True)
    current_amount= models.IntegerField(null=True)
    goal= models.IntegerField(null=True)
    donators= models.IntegerField(null=True)
    days_active= models.IntegerField(null=True)
    days_created= models.IntegerField(null=True)
    title= models.TextField(null=True)
    description= models.TextField(null=True)
    has_beneficiary=  models.BooleanField()
    media_type= models.IntegerField(null=True)
    project_type= models.IntegerField(null=True)
    turn_off_donations= models.BooleanField()
    user_id= models.IntegerField(null=True)
    user_first_name= models.TextField(null=True)
    user_last_name= models.TextField(null=True)
    user_facebook_id= models.TextField(null=True)
    user_profile_url= models.TextField(null=True)
    visible_in_search= models.BooleanField()
    status= models.IntegerField(null=True)
    deactivated= models.BooleanField()
    state= models.TextField(null=True)
    is_launched= models.BooleanField()
    campaign_image_url= models.TextField(null=True) 
    created_at= models.TextField(null=True)
    launch_date= models.TextField(null=True)
    campaign_hearts= models.IntegerField(null=True)
    social_share_total= models.IntegerField(null=True)
    social_share_last_update= models.TextField(null=True)
    location_city= models.TextField(null=True)
    location_country= models.TextField(null=True)
    location_zip= models.TextField(null=True)
    is_charity= models.BooleanField()
    charity_valid= models.BooleanField()
    charity_npo_id= models.TextField(null=True)
    charity_name= models.TextField(null=True)
    velocity= models.IntegerField(null=True)

