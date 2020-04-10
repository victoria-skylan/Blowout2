# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from INTEX.models import campaigns, Person
from INTEX.serializers import CampaignsSerializer, PersonSerializer
import json
from django.contrib.postgres.fields import JSONField

class CampaignList(APIView):
    @csrf_exempt
    def get(self, request, format=None):
        camp = campaigns.objects.all()
        serializer = CampaignsSerializer(camp, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = CampaignsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) #no json response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CampaignDetail(APIView):
    @csrf_exempt
    def get(self, request, pk, format=None):
        camp = campaigns.objects.get(id=pk)
        serializer = CampaignsSerializer(camp)
        return Response(serializer.data)

class CreateUser(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        body = json.loads(request.body)
        if User.objects.filter(username=body['email']).exists():
            return Response("Email is already in use")
        else:
            user = User.objects.create_user(body['email'], body['email'], body['password'])
            return Response(200)
    @csrf_exempt
    def get(self, request, format=None):
        body = json.loads(request.body)
        user = authenticate(username=body['email'], password=body['password'])
        if user is not None:
            if user.has_perm('INTEX.add_campaigns'):
                return Response(100)
            else:
                return Response(200)
        else:
            return Response("Invalid Credentials") 
    