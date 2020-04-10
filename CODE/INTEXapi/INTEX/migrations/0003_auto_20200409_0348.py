# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-09 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INTEX', '0002_auto_20200409_0307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaigns',
            name='auto_fb_post_mode',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='campaign_hearts',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='campaign_image_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='category',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='category_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='charity_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='charity_npo_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='collected_date',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='created_at',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='currencycode',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='current_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='days_active',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='days_created',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='donators',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='goal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='launch_date',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='location_city',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='location_country',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='location_zip',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='media_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='project_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='social_share_last_update',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='social_share_total',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='state',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='status',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='title',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='user_facebook_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='user_first_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='user_last_name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='user_profile_url',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='campaigns',
            name='velocity',
            field=models.IntegerField(null=True),
        ),
    ]
