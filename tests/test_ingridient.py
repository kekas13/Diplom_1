import unittest

from ..ingredient import Ingredient


class TestIngredient(unittest.TestCase):

    def test_init_type(self):
        for ingredient_type, name, price in [('Соус', 'Spicy-X', 1.5)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertEqual(Ingredient(ingredient_type, name, price).get_type(), ingredient_type)

    def test_init_name(self):
        for ingredient_type, name, price in [('Соус', 'Spicy-X', 1.5)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertEqual(Ingredient(ingredient_type, name, price).get_name(), name)

    def test_init_price(self):
        for ingredient_type, name, price in [('Соус', 'Spicy-X', 1.5)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertEqual(Ingredient(ingredient_type, name, price).get_price(), price)

    def test_check_type_ingredient_type(self):
        for ingredient_type, name, price in [('Соус', 'Spicy-X', 1.5)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertIsInstance(Ingredient(ingredient_type, name, price).get_type(), str)

    def test_check_name_type(self):
        for ingredient_type, name, price in [('Соус', 'Spicy-X', 1.5)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertIsInstance(Ingredient(ingredient_type, name, price).get_name(), str)

    def test_check_price_type(self):
        for ingredient_type, name, price in [('Соус', 'Spicy-X', 1.5)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertIsInstance(Ingredient(ingredient_type, name, price).get_price(), float)


class TestNegativeIngredient(unittest.TestCase):

    def test_check_type_ingredient_type(self):
        for ingredient_type, name, price in [(123, None, 0)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertNotIsInstance(Ingredient(ingredient_type, name, price).get_type(), str)

    def test_check_name_type(self):
        for ingredient_type, name, price in [(123, None, 0)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertNotIsInstance(Ingredient(ingredient_type, name, price).get_name(), str)

    def test_check_price_type(self):
        for ingredient_type, name, price in [(123, None, 0)]:
            with self.subTest(ingredient_type=ingredient_type, name=name, price=price):
                self.assertNotIsInstance(Ingredient(ingredient_type, name, price).get_price(), float)
