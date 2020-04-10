from rest_framework import serializers
from INTEX.models import  User, campaigns

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

class CampaignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = campaigns
        fields = [ 'id', 'url', 'auto_fb_post_mode',
        'collected_date',
        'category_id',
        'category',
        'currencycode',
        'current_amount',
        'goal',
        'donators',
        'days_active',
        'days_created',
        'title',
        'description',
        'has_beneficiary',
        'media_type',
        'project_type',
        'turn_off_donations',
        'user_id',
        'user_first_name',
        'user_last_name',
        'user_facebook_id',
        'user_profile_url',
        'visible_in_search',
        'status',
        'deactivated',   'state',
        'is_launched',
        'campaign_image_url',
        'created_at',
        'launch_date',
        'campaign_hearts',
        'social_share_total',
        'social_share_last_update',
        'location_city',
        'location_country',
        'location_zip',
        'is_charity',
        'charity_valid',
        'charity_npo_id',
        'charity_name',
        'velocity']