from django.test import TestCase
from ..models import Food

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
            marshmellow.__str__(), "Marshmellow")
        self.assertEqual(
            escargot.name, "Escargot")
