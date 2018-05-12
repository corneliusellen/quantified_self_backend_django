import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Food
from ..serializers import FoodSerializer
import code

client = Client()

class GetAllFoodsTest(TestCase):
    def setUp(self):
        Food.objects.create(
            name='Graham Crackers',
            calories=150)
        Food.objects.create(
            name='TimTams',
            calories=500)

    def test_get_all_foods(self):
        response = client.get(reverse('get_post_food'))
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetOneFoodTest(TestCase):
    def setUp(self):
        self.pudding = Food.objects.create(
            name='Pudding',
            calories=500)
        self.radishes = Food.objects.create(
            name='Radishes',
            calories=150)

    def test_get_one_food_valid(self):
        response = client.get(reverse('get_delete_update_food', kwargs={'pk': self.radishes.pk}))
        food = Food.objects.get(pk=self.pudding.pk)
        serializer = FoodSerializer(food)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_food_invalid(self):
        response = client.get(reverse('get_delete_update_food', kwargs={'pk': 5}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
