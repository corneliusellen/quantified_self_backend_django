from django.test import TestCase
from ..models import Food
from ..models import Meal

class FoodTest(TestCase):

    def setUp(self):
        Food.objects.create(
            name='Marshmellow',
            calories=200)
        Food.objects.create(
            name='Escargot',
            calories=900)

    def test_food_name(self):
        marshmellow = Food.objects.get(name='Marshmellow')
        escargot = Food.objects.get(name='Escargot')
        self.assertEqual(
            marshmellow.__str__(), 'Marshmellow')
        self.assertEqual(
            escargot.name, 'Escargot')

class MealTest(TestCase):

    def setUp(self):
        Meal.objects.create(
            name='Dinner')

    def test_meal_name(self):
        dinner = Meal.objects.get(name='Dinner')
        self.assertEqual(
            dinner.name, 'Dinner')

class MealFoods(TestCase):

    def setUp(self):
        marshmellow = Food.objects.create(
            name='Marshmellow',
            calories=200)
        dinner = Meal.objects.create(
            name='Dinner')
        dinner.foods.add(marshmellow)

    def test_mealfoods_name(self):
        meal = Meal.objects.get(name='Dinner')
        food = Food.objects.get(name='Marshmellow')
        self.assertEqual(
            meal.foods.all()[:1].get(), food)
