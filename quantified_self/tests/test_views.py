import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Food
from ..models import Meal
from ..serializers import FoodSerializer
from ..serializers import MealSerializer
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
        response = client.get(reverse('get_delete_update_food', kwargs={'pk': self.pudding.pk}))
        food = Food.objects.get(pk=self.pudding.pk)
        serializer = FoodSerializer(food)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_food_invalid(self):
        response = client.get(reverse('get_delete_update_food', kwargs={'pk': 3005}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewFoodTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            'food': {
                'name': 'Muffin',
                'calories': 400
            }
        }
        self.invalid_payload = {
            'food': {
                'name': '',
                'calories': 2
            }
        }

    def test_create_food_valid(self):
        response = client.post(
            reverse('get_post_food'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        food = Food.objects.get(pk=1)
        serializer = FoodSerializer(food)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)


    def test_create_food_invalid(self):
        response = client.post(
            reverse('get_post_food'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateFoodTest(TestCase):

    def setUp(self):
        self.almonds = Food.objects.create(
            name='Almonds',
            calories=500)
        self.valid_payload = {
            'name': 'Almonds',
            'calories': 10
        }
        self.invalid_payload = {
            'name': '',
            'calories': 7
        }

    def test_update_food_valid(self):
        response = client.patch(
            reverse('get_delete_update_food', kwargs={'pk': self.almonds.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        food = Food.objects.get(pk=self.almonds.pk)
        serializer = FoodSerializer(food)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_update_food_invalid(self):
        response = client.patch(
            reverse('get_delete_update_food', kwargs={'pk': self.almonds.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteFoodTest(TestCase):

    def setUp(self):
        self.berries = Food.objects.create(
            name='Strawberries', calories='40')

    def test_delete_food(self):
        response = client.delete(
        reverse('get_delete_update_food', kwargs={'pk': self.berries.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllMealsTest(TestCase):

    def setUp(self):
        marshmellow = Food.objects.create(
            name='Marshmellow',
            calories=200)
        fish = Food.objects.create(
            name='Fish',
            calories=20)
        dinner = Meal.objects.create(
            name='Dinner')
        breakfast = Meal.objects.create(
            name='Breakfast')
        dinner.foods.add(marshmellow)
        breakfast.foods.add(fish)

    def test_get_all_meals(self):
        response = client.get(reverse('get_meals'))
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetOneMealTest(TestCase):

    def setUp(self):
        marshmellow = Food.objects.create(
            name='Marshmellow',
            calories=200)
        fish = Food.objects.create(
            name='Fish',
            calories=20)
        self.dinner = Meal.objects.create(
            name='Dinner')
        self.breakfast = Meal.objects.create(
            name='Breakfast')
        self.dinner.foods.add(marshmellow)
        self.breakfast.foods.add(fish)

    def test_get_one_meal(self):
        response = client.get(reverse('get_meal_foods', kwargs={'pk': self.dinner.pk}))
        meal = Meal.objects.get(pk=self.dinner.pk)
        serializer = MealSerializer(meal)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
