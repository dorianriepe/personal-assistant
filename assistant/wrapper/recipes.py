import requests
import json
from random import randint
import os


class Recipes:
    
    __instance = None

    @staticmethod
    def getInstance(recipe_url="https://api.edamam.com/search"):
        if Recipes.__instance is None:
            Recipes(recipe_url)
        return Recipes.__instance

    def __init__(self, recipe_url="https://api.edamam.com/search"):
        if Recipes.__instance is None:
            self.recipe_url = recipe_url
            Recipes.__instance = self
        else:
            raise Exception("This class is a singleton!")

    def get_response(self, querystring):
        return requests.request("GET", self.recipe_url, params=querystring).json()

    def get_recipe_by_uri(self, uri):
        querystring = {"app_id": os.environ.get('RECIPE_APP_ID'),
                       "app_key": os.environ.get('RECIPE_APP_KEY'),
                       "r": uri}

        response_json = self.get_response(querystring)

        if response_json:
            try:
                recipe = response_json[0]

                return {"recipe_uri": recipe["uri"],
                        "recipe_name": recipe["label"],
                        "recipe_image": recipe["image"],
                        "recipe_url": recipe["url"],
                        "recipe_calories": int(recipe["calories"]),
                        "recipe_ingredients": recipe["ingredientLines"],
                        "recipe_time": recipe["totalTime"]
                        }
            except:
                return

        else:
            print("An error occured")
            return

    def get_recipe_by_ingredients(self, ingredients, random_recipes=True, diet="balanced", health=None):

        # ingredients: comma seperated string
        # random_recipes: for multiple searches with same query
        # possible values for diet: balanced, high-protein, low-carb, low-fat
        # possible values for health; alcohol-free, vegan, vegetarian, peanut-free, sugar-conscious, tree-nut-free
        # full docu: https://developer.edamam.com/edamam-docs-recipe-api

        querystring = {"app_id": os.environ.get('RECIPE_APP_ID'),
                       "app_key": os.environ.get('RECIPE_APP_KEY'),
                       "q": ingredients,
                       "diet": diet}
        if health:
            querystring["health"] = health

        response_json = self.get_response(querystring)

        if response_json:
            recipe_number = 0
            if random_recipes:
                recipe_number = randint(0, 9)

            try:
                recipe = response_json['hits'][recipe_number]['recipe']

                return {"recipe_uri": recipe["uri"],
                        "recipe_name": recipe["label"],
                        "recipe_image": recipe["image"],
                        "recipe_url": recipe["url"],
                        "recipe_calories": int(recipe["calories"]),
                        "recipe_ingredients": recipe["ingredientLines"],
                        "recipe_time": recipe["totalTime"]
                        }
            except:
                return

        else:
            print("An error occured")
            return
