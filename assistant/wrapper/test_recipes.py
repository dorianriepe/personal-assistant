import unittest
from unittest import TestCase
from unittest.mock import patch
import json
import os

from recipes import Recipes


class TestRecipes(TestCase):

    @patch('recipes.Recipes.get_response')
    def test_get_recipe_by_ingredients1(self, mock_get_response):
        inst = Recipes.getInstance('http://127.0.0.1')
        test_path = os.path.join("test-responses-recipes", "response1.json")
        file = open(test_path, "r")
        ml = json.loads(file.read())
        file.close()

        mock_get_response.return_value = ml

        res = inst.get_recipe_by_ingredients(
            "noodles, chicken, pepper, milk", random_recipes=False)
        expected_res = {'recipe_uri': 'http://www.edamam.com/ontologies/edamam.owl#recipe_35a93fee16e7683b1ece4d9070f974f1', 'recipe_name': 'Chicken, Spinach, And Noodle Casserole', 'recipe_image': 'https://www.edamam.com/web-img/bf8/bf8173103cd9cffd0da967b1cbb93636.jpg', 'recipe_url': 'http://www.realsimple.com/food-recipes/browse-all-recipes/chicken-noodle-casserole-00100000075552/index.html',
                        'recipe_calories': 3902, 'recipe_ingredients': ['6 tablespoons unsalted butter', '1/4 cup all-purpose flour', '4 cups whole milk', '1 cup sour cream', 'kosher salt and black pepper', '12 ounces egg noodles', '4 slices sandwich bread', '2 cups shredded cooked chicken or rotisserie chicken', '5 ounces baby spinach, chopped', '2 teaspoons dried thyme'], 'recipe_time': 0.0}


        self.assertEqual(expected_res, res)

    @patch('recipes.Recipes.get_response')
    def test_get_recipe_by_ingredients2(self, mock_get_response):

        inst = Recipes.getInstance('http://127.0.0.1')
        test_path = os.path.join("test-responses-recipes", "response2.json")
        file = open(test_path, "r")
        ml = json.loads(file.read())
        file.close()

        mock_get_response.return_value = ml

        res = inst.get_recipe_by_ingredients("noodles, chicken, pepper, milk", random_recipes=False, diet="low-fat")
        expected_res = {'recipe_uri': 'http://www.edamam.com/ontologies/edamam.owl#recipe_696ea2fc73f79991174e2a7b650b48f9', 'recipe_name': 'Tuna Casserole', 'recipe_image': 'https://www.edamam.com/web-img/ea7/ea714deca9d0a2fc9067263de1d7db55.jpeg', 'recipe_url': 'https://www.foodnetwork.com/recipes/tuna-casserole-recipe-1938022', 'recipe_calories': 3317, 'recipe_ingredients': ['5 slices whole-wheat bread, crusts included', '1 tablespoon canola oil','1 small onion, chopped (about 1 cup)', '1 large stalk celery, finely diced (about 1/2 cup)', '1 (10-ounce) box white mushroom, stemmed and chopped (about 2 1/2 cups)', '1/4 cup all-purpose flour', '3 cups 1 percent milk', '1 cup low-sodium chicken broth or vegetable broth', '3/4 teaspoon salt', '1/4 teaspoon ground black pepper', '1/2 pound whole-wheat fettuccine noodles, broken into thirds and cooked according to package directions', '1 (10-ounce) box frozen chopped broccoli, thawed', '1 (10-ounce) box frozen peas, thawed', '4 (6-ounce) cans chunk light tuna in water, drained'], 'recipe_time': 60.0}


        self.assertEqual(expected_res, res)

    @patch('recipes.Recipes.get_response')
    def test_get_recipe_by_ingredients3(self, mock_get_response):
        inst = Recipes.getInstance('http://127.0.0.1')
        test_path = os.path.join("test-responses-recipes", "response3.json")
        file = open(test_path, "r")
        ml = json.loads(file.read())
        file.close()

        mock_get_response.return_value = ml

        res = inst.get_recipe_by_ingredients("noodles, onion, pepper", random_recipes=False, health="vegan")
        expected_res = {'recipe_uri': 'http://www.edamam.com/ontologies/edamam.owl#recipe_abc04cbb4dec1b122e9fcdbd3c434184', 'recipe_name': 'Singapore Noodles With Tofu', 'recipe_image': 'https://www.edamam.com/web-img/727/7278fe73f2043c240b8070ea8a4f9a81.jpg', 'recipe_url': 'http://www.bbcgoodfood.com/recipes/10769/', 'recipe_calories': 975, 'recipe_ingredients': ['2 tsp reduced-salt soy sauce', '1 red pepper , thinly sliced', '100.0g fine rice noodles', '1 small chunk fresh root ginger , finely chopped', '100.0g mangetout', '1 tsp tikka masala paste', '100.0g bean sprouts', '2 tbsp sunflower oil', 'roughly chopped coriander and lime wedges, to serve', '140.0g firm tofu', '1 tbsp sweet chilli sauce', '3 spring onions , shredded'], 'recipe_time': 0.0}

        self.assertEqual(expected_res, res)

    @patch('recipes.Recipes.get_response')
    def test_get_recipe_by_ingredients4(self, mock_get_response):
        inst = Recipes.getInstance('http://127.0.0.1')
        test_path = os.path.join("test-responses-recipes", "response4.json")
        file = open(test_path, "r")
        ml = json.loads(file.read())
        file.close()

        mock_get_response.return_value = ml

        res = inst.get_recipe_by_ingredients("noodles, chicken, pepper, egg",
                                             random_recipes=False, health="vegan")
        expected_res = None

        self.assertEqual(expected_res, res)

    @patch('recipes.Recipes.get_response')
    def test_get_recipe_by_uri1(self, mock_get_response):
        inst = Recipes.getInstance('http://127.0.0.1')
        test_path = os.path.join("test-responses-recipes", "response5.json")
        file = open(test_path, "r")
        ml = json.loads(file.read())
        file.close()

        mock_get_response.return_value = ml
        res = inst.get_recipe_by_uri("http://www.edamam.com/ontologies/edamam.owl#recipe_35a93fee16e7683b1ece4d9070f974f1")
        expected_res = {'recipe_uri': 'http://www.edamam.com/ontologies/edamam.owl#recipe_35a93fee16e7683b1ece4d9070f974f1', 'recipe_name': 'Chicken, Spinach, And Noodle Casserole', 'recipe_image': 'https://www.edamam.com/web-img/bf8/bf8173103cd9cffd0da967b1cbb93636.jpg', 'recipe_url': 'http://www.realsimple.com/food-recipes/browse-all-recipes/chicken-noodle-casserole-00100000075552/index.html','recipe_calories': 3902, 'recipe_ingredients': ['6 tablespoons unsalted butter', '1/4 cup all-purpose flour', '4 cups whole milk', '1 cup sour cream', 'kosher salt and black pepper', '12 ounces egg noodles', '4 slices sandwich bread', '2 cups shredded cooked chicken or rotisserie chicken', '5 ounces baby spinach, chopped', '2 teaspoons dried thyme'], 'recipe_time': 0.0}

        self.assertEqual(expected_res, res)

if __name__ == '__main__':
    unittest.main()
