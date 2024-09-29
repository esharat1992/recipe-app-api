from django.test import SimpleTestCase
from app import calc


# test function
class AddNumTest(SimpleTestCase):
    def test_add(self):
        res = calc.add(5, 8)
        self.assertEqual(res, 13)

    def test_sub(self):
        res = calc.substract(10, 15)
        self.assertEqual(res, 5)
