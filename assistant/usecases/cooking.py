from wrapper.google_calendar import Calendar
from wrapper.recipes import Recipes
from wrapper.google_tasks import Tasks
import json
import datetime


class Cooking:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):

        if (context == "proactiveShoopingList" or context == "shoppingList"):
            response = self.shoppingList(text, context, preferences)
        elif (context == "proactiveCooking" or context == "cook"):
            response = self.askForCooking(text, context, preferences)
        elif (context == "spotify" or context == "playSpotify"):
            response = self.spotify(text, context, preferences)
        else:
            response = self.presentRecipe(preferences)

        # response = {
        #         "text": "Today you have planned spaghetti with tomato sauce. You don't have any appointments between 12am and 2pm. Shall I put the ingredients on the shopping list?",
        #         "html": "<p>Today you have planned spaghetti with tomato sauce. You don't have any appointments between 12:00 and 14:00. Shall I put the ingredients on the shopping list?<p>",
        #         "follow_up": "cooking",
        #         "context": "test"
        #     }

        return response

    def shoppingList(self, text, context, preferences):
        if context == "proactiveShoopingList":
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

                    endTimeL = list(endTime)
                    endTimeL[1] = str(int(endTimeL[1])+1)
                    newEndTime = "".join(endTimeL)
                    if (startTime < newEndTime):
                        endTime = None
                        startTime = None
                    break

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

        elif context == "shoppingList":
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

    def spotify(self, text, context, preferences):
        if (context == "spotify"):
            # shows user a playlist
            pass
        elif (context == "playSpotify"):
            # starts spotify playlist
            pass
        return response

    def askForCooking(self, text, context, preferences):
        if context == "proactiveCooking":
            # this is for a proactive call from client
            pass
        elif context == "cook":
            # this is for an answer
            pass
        return response

    def presentRecipe(self, preferences):

        return response
