from django.test import TestCase
from .models import Product

# Create your tests here.


class ProductTests(TestCase):
    """"Here We Will Define The Tests"""


def test_str(self):
    test_name = Product(name='A Product')
    self. assertEqual(str(test_name), 'A product')
