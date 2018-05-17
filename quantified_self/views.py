# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Food
from .serializers import FoodSerializer
from django.http import HttpResponse
import code

@api_view(['GET', 'DELETE', 'PATCH'])
def get_delete_update_food(request, pk):
    try:
        food = Food.objects.get(pk=pk)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FoodSerializer(food)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        food.delete()
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'PATCH':
        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_food(request):
    if request.method == 'GET':
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {
            'name': request.data.get('food').get('name'),
            'calories': request.data.get('food').get('calories'),
        }
        serializer = FoodSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
