# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer

@api_view(['GET', 'DELETE', 'PATCH'])
def get_delete_update_food(request, pk):
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({})
    elif request.method == 'DELETE':
        return Response({})
    elif rquest.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_food(request):
    if request.method == 'GET':
        return Response({})
    elif request.method == 'POST':
        return Response({})
