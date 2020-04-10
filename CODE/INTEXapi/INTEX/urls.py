from django.conf.urls import url, include
from django.contrib.auth.models import User
from INTEX import views
# from rest_framework import routers, serializers, viewsets
# from api import views



urlpatterns = [
    url('campaigns/', views.CampaignList.as_view(), name="campaignsList"),
    url('campaigns/<int:pk>/', views.CampaignDetail.as_view(), name="campaignDetail"),
    url('user/', views.CreateUser.as_view(), name="createUser"),
]