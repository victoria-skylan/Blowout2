#!/usr/bin/env python3
# initialize django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'INTEXapi.settings'
import django
import json
django.setup()

from INTEX.models import  Person, campaigns

def main():
    # createCamp()
    # createAdmin()

def createAdmin():
    p = Person()
    p.email = "1@gmail.com"
    p.password = "11111"
    p.admin = False
    p.save()
    for p in Person.objects.all():
        print(p.email, p.admin)


def createCamp():
    # campaigns.objects.all().delete() #!!!!!!!!
    with open('campaign.json') as json_file:
        data = json.load(json_file)
        for p in data:
            camp = campaigns()
            camp.id = p['id']
            camp.url = p['url']
            camp.auto_fb_post_mode = p['auto_fb_post_mode']
            camp.collected_date = p['collected_date']
            camp.category_id = p['category_id']
            camp.category = p['category'] 
            camp.currencycode = p['currencycode']
            camp.current_amount = p['current_amount']
            camp.goal = p['goal']
            camp.donators = p['donators']
            camp.days_active = p['days_active']
            camp.days_created = p['days_created']
            camp.title = p['title']
            camp.description = p['description']
            camp.default_url = p['default_url']
            camp.has_beneficiary = p['has_beneficiary']
            camp.media_type = p['media_type']
            camp.project_type = p['project_type']
            camp.turn_off_donations = p['turn_off_donations']
            camp.user_id = p['user_id']
            camp.user_first_name = p['user_first_name']
            camp.user_last_name = p['user_last_name']
            camp.user_facebook_id = p['user_facebook_id']
            camp.user_profile_url = p['user_profile_url']
            camp.visible_in_search = p['visible_in_search']
            camp.status = p['status']
            camp.deactivated = p['deactivated']
            camp.state = p['state']
            camp.is_launched = p['is_launched']
            camp.campaign_image_url = p['campaign_image_url']
            camp.created_at = p['created_at']
            camp.launch_date = p['launch_date']
            camp.campaign_hearts = p['campaign_hearts']
            camp.social_share_total = p['social_share_total']
            camp.social_share_last_update = p['social_share_last_update']
            camp.location_city = p['location_city']
            camp.location_country = p['location_country']
            camp.location_zip = p['location_zip']
            camp.is_charity = p['is_charity']
            camp.charity_valid = p['charity_valid']
            camp.charity_npo_id = p['charity_npo_id']
            camp.charity_name = p['charity_name']
            camp.velocity = p['velocity']
            camp.save()
    for camp in campaigns.objects.all():
        print(camp.id)

# bootstrap
if __name__ == '__main__':
    main()
