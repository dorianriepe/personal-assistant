from wrapper.google_calendar import Calendar
from wrapper.recipes import Recipes
from wrapper.google_tasks import Tasks
import json
import datetime


class Cooking:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):

        if (context == "proactiveShoopingList"):
            response = self.shoppingList(text, preferences)
        elif (context == "shoppingList"):
            response = self.shoppingListResponseHandling(text)
        elif (context == "proactiveCooking"):
            response = self.askForCooking(text, preferences)
        elif (context == "cook"):
            response = self.cookNow(text, preferences)
        elif (context == "spotify"):
            response = self.spotify(text, context, preferences)
        elif (context == "playSpotify"):
            response = self.playSpotify(text, preferences)
        else:
            response = self.presentRecipe(preferences)

        # response = {
        #         "text": "Today you have planned spaghetti with tomato sauce. You don't have any appointments between 12am and 2pm. Shall I put the ingredients on the shopping list?",
        #         "html": "<p>Today you have planned spaghetti with tomato sauce. You don't have any appointments between 12:00 and 14:00. Shall I put the ingredients on the shopping list?<p>",
        #         "follow_up": "cooking",
        #         "context": "test"
        #     }

        return response

    def shoppingList(self, text, preferences):
        # this is for a proactive call from client
        # look calendar up
        # response = [{'title': 'Datenbanken', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]

        # search for a planned meal in calendar
        calendar = Calendar("DHBW6")
        events = calendar.get_events_today().json()
        meal = None
        for event in events:
            if "Meal" in event.title:
                meal = event.title[6:]
                break

        # look for next free time
        endTime = None
        startTime = None
        for event in events:
            if not endTime:
                endTime = event.end
            else:
                startTime = event.start

                diff = datetime.datetime.strptime(
                    endTime, '%H:%M') - datetime.datetime.strptime(startTime, '%H:%M')
                if diff.total_seconds() < 3600:  # One hour
                    endTime = event.end
                else:
                    break

        # check for set free time (if... else...)

        if meal:
            # search for recipe for planned meal
            recipe_engine = Recipes.getInstance()
            search_text = meal.replace(" ", ", ")
            diet = preferences.diet
            health = preferences.health
            recipe = recipe_engine.get_recipe_by_ingredients(
                search_text, False, diet, health)

            # write ingredients to shopping list
            ingredients_list = recipe.recipe_ingredients
            google_tasks = Tasks()
            today = datetime.date.today()
            for ingredient in ingredients_list:
                google_tasks.add_task_to_list(
                    "shoppingList"+today, ingredient)

            response = {
                "text": "Today you have planned" + recipe.recipe_name + ". You don't have any appointments between" + endTime + "and" + startTime + ". Shall I put the ingredients on the shopping list?",
                        "html": "<p>Today you have planned" + recipe.recipe_name + ". You don't have any appointments between" + endTime + "and" + startTime + ". Shall I put the ingredients on the shopping list?<p>",
                        "follow_up": "cooking",
                        "context": "shoppingList"
            }

        else:
            # get a random recipe
            diet = preferences.diet
            health = preferences.health
            recipe = recipe_engine.get_recipe_by_ingredients(
                "rice", True, diet, health)

            # write ingredients to shopping list
            ingredients_list = recipe.recipe_ingredients
            google_tasks = Tasks()
            today = datetime.date.today()
            for ingredient in ingredients_list:
                google_tasks.add_task_to_list(
                    "shoppingList"+today, ingredient)

            response = {
                "text": "Today you haven't planned anything to eat. But I found a recipe for" + recipe.recipe_name + ". You don't have any appointments between" + endTime + "and" + startTime + ". Shall I put the ingredients on the shopping list?",
                        "html": "<p>Today you haven't planned anything to eat. But I found a recipe for" + recipe.recipe_name + ". You don't have any appointments between" + endTime + "and" + startTime + ". Shall I put the ingredients on the shopping list?<p>",
                        "follow_up": "cooking",
                        "context": "shoppingList"
            }

        return response

    def shoppingListResponseHandling(self, text):
        if ("no" in text):
            google_tasks = Tasks()
            today = datetime.date.today()
            google_tasks.delete_list("shoppingList"+today)

        null = None
        response = {
            "text": null,
            "html": null,
            "follow_up": null,
            "context": null
        }

        return response

    def spotify(self, text, preferences):
        # shows user a playlist
        return response

    def playSpotify(self, text, preferences):
        # starts spotify playlist
        pass
        return response

    def askForCooking(self, text, context, preferences):
        # this is for a proactive call from client
        pass
        return response

    def cookNow(self, text, preferences):
        # this is for an answer
        pass
        return response

    def presentRecipe(self, preferences):

        return response
