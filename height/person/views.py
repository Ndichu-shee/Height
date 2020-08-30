from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

@api_view(['POST'])
def total(weightPerson):
    try:
        weight=json.loads(weightPerson.body)
        height=str(weight/15)
        return JsonResponse("The maximum height is' " +height+ "metres" , safe=False)
    except ValueError as e:
            return Response(e.args[0].status.HTTP_400_BAD_REQUEST)