import unittest

from ..database import Database


class TestDatabase(unittest.TestCase):

    def test_available_buns(self):
        buns_list = lambda: [i.get_name() for i in Database().available_buns()]
        for bun in ['black bun']:
            with self.subTest(bun=bun):
                self.assertIn(bun, buns_list())

    def test_available_ingredients(self):
        ingredients_list = lambda: [i.get_name() for i in Database().available_ingredients()]
        for ingredient in ['hot sauce']:
            with self.subTest(ingredient=ingredient):
                self.assertIn(ingredient, ingredients_list())
