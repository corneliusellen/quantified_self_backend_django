import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Food
from ..serializers import FoodSerializer

client = Client()

class GetAllFoodsTest(TestCase):
    def setUp(self):
        Food.objects.create(
            name='Pudding',
            calories=500)
        Food.objects.create(
            name='Radishes',
            calories=150)

    def test_get_all_foods(self):
        response = client.get(reverse('get_post_food'))
        foods = Food.objects.all()
        serializer = FoodSerializer(foods, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
