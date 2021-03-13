from wrapper.google_calendar import Calendar
from wrapper.recipes import Recipes
from wrapper.google_tasks import Tasks
from wrapper.html_response import HTMLResponseBuilder
from wrapper.spotify import Spotify
import json
import datetime
import random

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
        elif (context == "spotify"):
            response = self.spotify(text, preferences)
        elif ("playSpotify" in context):
            response = self.playSpotify(text, context, preferences)
        else:
            response = self.cookNow(text, preferences)

        return response

    def shoppingList(self, text, preferences):
        # this is for a proactive call from client
        # look calendar up
        # response = [{'title': 'Datenbanken', 'location': 'https://dhbw-stuttgart.zoom.us/j/99643057619', 'start': '10:00', 'end': '12:30'}, {'title': 'Security', 'location': '', 'start': '13:15', 'end': '15:45'}, {'title': 'Zero Knowledge', 'location': '', 'start': '13:00', 'end': '15:30'}]

        # search for a planned meal in calendar
        calendar = Calendar("Cooking")
        events = calendar.get_events_today()
        meal = None
        if len(events) > 0: 
            meal = events[0]["title"]

        # look for next free time
        endTime = None
        startTime = None
        for event in events:
            if not endTime:
                endTime = event["end"]
            else:
                startTime = event["start"]

                diff = datetime.datetime.strptime(
                    endTime, '%H:%M') - datetime.datetime.strptime(startTime, '%H:%M')
                if diff.total_seconds() < 3600:  # One hour
                    endTime = event["end"]
                else:
                    break

        # check for set free time (if... else...)

        recipe_engine = Recipes.getInstance()

        if meal:
            # search for recipe for planned meal
            diet = preferences["diet"]
            health = preferences["health"]
            recipe = recipe_engine.get_recipe_by_ingredients(
                meal, False, diet, health)

            # write ingredients to shopping list
            ingredients_list = recipe["recipe_igredients"]
            google_tasks = Tasks()
            today = datetime.date.today()
            for ingredient in ingredients_list:
                google_tasks.add_task_to_list(
                    "shoppingList"+today, ingredient)

            response = {
                "text": "Today you have planned " + recipe["recipe_name"] + ". You don't have any appointments between " + endTime + "and " + startTime + ". Shall I put the ingredients on the shopping list?",
                        "html": "<p>Today you have planned " + recipe["recipe_name"] + ". You don't have any appointments between " + endTime + "and " + startTime + ". Shall I put the ingredients on the shopping list?<\p>",
                        "follow_up": "cooking",
                        "context": "shoppingList"
            }

        else:
            # get a random recipe
            diet = preferences["diet"]
            health = preferences["health"]
            ingredients = ['rice', 'potato', 'chicken', 'noodles']
            recipe = recipe_engine.get_recipe_by_ingredients(random.choice(ingredients), True, diet, health)

            # write ingredients to shopping list
            ingredients_list = recipe["recipe_ingredients"]
            google_tasks = Tasks()
            today = datetime.date.today()
            for ingredient in ingredients_list:
                google_tasks.add_task_to_list(
                    "shoppingList"+today, ingredient)

            response = {
                "text": "Today you haven't planned anything to eat. But I found a recipe for " + recipe["recipe_name"] + ". You don't have any appointments between " + endTime + "and " + startTime + ". Shall I put the ingredients on the shopping list?",
                        "html": "<p>Today you haven't planned anything to eat. But I found a recipe for " + recipe["recipe_name"] + ". You don't have any appointments between " + endTime + "and " + startTime + ". Shall I put the ingredients on the shopping list?<\p>",
                        "follow_up": "cooking",
                        "context": "shoppingList"
            }

        return response

    def shoppingListResponseHandling(self, text):
        
        negative_text = ['no', 'dont']
        if any(t in text for t in negative_text):

            google_tasks = Tasks()
            today = datetime.date.today()
            google_tasks.delete_list("shoppingList"+today)

        response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }

        return response

    def spotify(self, text, preferences):
        negative_text = ['no', 'dont']
        if any(t in text for t in negative_text):

            response = {
                "text": None,
                "html": None,
                "follow_up": None,
                "context": None
            }

        else:
            html_builder = HTMLResponseBuilder()

            music = Spotify()
            playlist = music.get_playlist("cooking")[0]

            text = "I found this playlist. Do you want me to start the playlist?"
            html = html_builder.img_title_subtitle(
                        text = "I found this playlist. Do you want me to start the playlist?",
                        title = playlist["name"],
                        subtitle = "by " + playlist["author"],
                        image_url = playlist["image_url"],
                        link = playlist["uri"]
                    )

            response = {
                "text": text,
                "html": html,
                "follow_up": "cooking",
                "context": "playSpotify" + playlist["uri"]
            }

        return response

    def playSpotify(self, text, context, preferences):
        positive_text = ['yes', 'please', 'ok', 'sure']
        if any(t in text for t in positive_text):

            music = Spotify()
            uri = context[11:]
            music.start_playback(uri)

        response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }

        return response

    #  this is for a proactive call from client
    def askForCooking(self, text, context, preferences):

        response = {
            "text": "Hey, have you already cooked? If not, would you like to cook now?",
            "html": "<p>Hey, have you already cooked? If not, would you like to cook now?<\p>",
            "follow_up": "cooking",
            "context": "cook"
        }

        return response

    def cookNow(self, text, preferences):
        
        negative_text = ['no', 'not']
        if any(t in text for t in negative_text):
            response = {
                "text": None,
                "html": None,
                "follow_up": None,
                "context": None
            }

        else:
            # search for a planned meal in calendar
            calendar = Calendar("Cooking")
            events = calendar.get_events_today()
            meal = None
            if len(events) > 0: 
                meal = events[0]["title"]
            html_builder = HTMLResponseBuilder()
            recipe_engine = Recipes.getInstance()

            if meal:
                # search for recipe for planned meal
                diet = preferences.get("diet", "balanced")
                health = preferences.get("health", None)
                recipe = recipe_engine.get_recipe_by_ingredients(meal, False, diet, health)

            else:
                # get a random recipe
                diet = preferences.get("diet", "balanced")
                health = preferences.get("health", None)
                ingredients = ['rice', 'potato', 'chicken', 'noodles']
                recipe = recipe_engine.get_recipe_by_ingredients(random.choice(ingredients), True, diet, health)

            # write ingredients to shopping list
            ingredients_list = recipe["recipe_ingredients"]
            google_tasks = Tasks()
            today = datetime.date.today()
            for ingredient in ingredients_list:
                google_tasks.add_task_to_list(
                    "shoppingList"+str(today), ingredient)

            text = "Today you have planned" + recipe["recipe_name"] + ". Would you like to listion to some music?"

            html = html_builder.img_title_subtitle(
                    text = "Here is your recipe. Would you like to listion to some music?",
                    title = recipe["recipe_name"],
                    subtitle = str(int(recipe["recipe_time"]))+" min, " + str(recipe["recipe_calories"]) + " calories",
                    image_url =recipe["recipe_image"],
                    link = recipe["recipe_url"]
                )

            response = {
                "text": text,
                "html": html,
                "follow_up": "cooking",
                "context": "spotify"
            }

        return response
