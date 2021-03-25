from wrapper.google_calendar import Calendar
from wrapper.recipes import Recipes
from wrapper.google_tasks import Tasks
from wrapper.html_response import HTMLResponseBuilder
from wrapper.spotify import Spotify
import json
import datetime
import random


class Cooking:

    __instance = None

    @staticmethod
    def getInstance():
        if Cooking.__instance is None:
            Cooking()
        return Cooking.__instance

    def __init__(self):
        if Cooking.__instance is None:
            Cooking.__instance = self
        else:
            raise Exception("This class is a singleton!")

    def handle(self, text, context, preferences):
        """handle function call the right method

        Args:
            text ([type]): spoken text from user
            context ([type]): context in which user currently is
            preferences (dict): all user preferences, which are collected over the frontend

        Returns:
            response (dict): the response including speaking text, html, context and follow_up usecase (cooking)
        """

        if (context == "proactiveShoopingList"):
            response = self.shoppingList(preferences)
        elif (context == "shoppingList"):
            response = self.shoppingListResponseHandling(text)
        elif (context == "proactiveCooking"):
            response = self.askForCooking()
        elif (context == "spotify"):
            response = self.spotify(text, preferences)
        elif (context and ("playSpotify" in context)):
            response = self.playSpotify(text, context, preferences)
        else:
            response = self.cookNow(text, preferences)

        return response

    def shoppingList(self, preferences):
        """Method for a proactive call from client: \
            Looks up planned meals and next meetings and write ingredients to shopping list.

        Args:
            preferences (dict): all user preferences, which are collected over the frontend

        Returns:
            response (dict): the response including speaking text, html, context and follow_up usecase (cooking)
        """
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

        # This is just for prototype reasons:
        if (not endTime) or (not startTime):
            endTime = "14:00"
            startTime = "16:00"

        recipe_engine = Recipes.getInstance()

        if meal:  # a plnned meal in calendar is found
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
                    "shoppingList" + today.strftime("%d/%m/%Y"), ingredient)

            response = {
                "text": "Today you have planned " + recipe["recipe_name"] + ". You don't have any appointments between " + endTime + "and " + startTime + ". Shall I put the ingredients on the shopping list, " + preferences["name"] + "?",
                        "html": "<p>Shall I put the ingredients on the shopping list, " + preferences["name"] + "?</p>",
                        "follow_up": "cooking",
                        "context": "shoppingList"
            }

        else:  # no meal is found in calendar
            # get a random recipe
            diet = preferences["diet"]
            health = preferences["health"]
            ingredients = ['rice', 'potato', 'chicken', 'noodles']
            recipe = recipe_engine.get_recipe_by_ingredients(
                random.choice(ingredients), False, diet, health)

            # write ingredients to shopping list
            ingredients_list = recipe["recipe_ingredients"]
            google_tasks = Tasks()
            today = datetime.date.today()
            for ingredient in ingredients_list:
                google_tasks.add_task_to_list(
                    "shoppingList" + today.strftime("%d/%m/%Y"), ingredient)

            response = {
                "text": "Today you haven't planned anything to eat. But I found a recipe for " + recipe["recipe_name"] + ". You don't have any appointments between " + endTime + "and " + startTime + ". Shall I put the ingredients on the shopping list, " + preferences["name"] + "?",
                        "html": "<p>Shall I put the ingredients on the shopping list, " + preferences["name"] + "?</p>",
                        "follow_up": "cooking",
                        "context": "shoppingList"
            }

        return response

    def shoppingListResponseHandling(self, text):
        """delete the by the function "ShoopingList" created shopping list, if user doesn't want to create a shooping list.

        Args:
            text (string): spoken text from user

        Returns:
            response (dict): the response including speaking text, html, context and follow_up usecase (cooking)
        """
        negative_text = ['no', 'dont']
        if any(t in text for t in negative_text):

            google_tasks = Tasks()
            today = datetime.date.today()
            google_tasks.delete_list("shoppingList"+today.strftime("%d/%m/%Y"))

        response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }

        return response

    def spotify(self, text, preferences):
        """If wanted, the function returns a cooking spotify playlist

        Args:
            text ([type]): spoken text from the user
            preferences (dict): all user preferences, which are collected over the frontend

        Returns:
            response (dict): the response including speaking text, html, context and follow_up usecase (cooking)
        """

        negative_text = ['no', 'dont']
        if any(t in text for t in negative_text):
            # no playlist is wished
            response = {
                "text": None,
                "html": None,
                "follow_up": None,
                "context": None
            }

        else:  # spotify playlist is wished
            html_builder = HTMLResponseBuilder()

            # find a playlist
            music = Spotify()
            playlist = music.get_playlist("cooking")[0]

            # build response
            text = "I found this playlist. Do you want me to start the playlist?"
            html = html_builder.img_title_subtitle(
                text="I found this playlist. Do you want me to start the playlist?",
                title=playlist["name"],
                subtitle="by " + playlist["author"],
                image_url=playlist["image_url"],
                link=playlist["uri"]
            )

            response = {
                "text": text,
                "html": html,
                "follow_up": "cooking",
                "context": "playSpotify" + playlist["uri"]
            }

        return response

    def playSpotify(self, text, context, preferences):
        """start the given sporify playlist if wanted

        Args:
            text (string): spoken text from user
            context (string): the context contains the playlist uri which is used to start the playlist on the device
            preferences (dict): all user preferences, which are collected over the frontend

        Returns:
            response (dict): the response including speaking text, html, context and follow_up usecase (cooking)
        """
        positive_text = ['yes', 'please', 'ok', 'sure']
        if any(t in text for t in positive_text):

            # plays music if this is wanted
            music = Spotify()
            uri = context[11:]
            music.start_playback(uri)

        # send response anyway
        response = {
            "text": None,
            "html": None,
            "follow_up": None,
            "context": None
        }

        return response

    #  this is for a proactive call from client
    def askForCooking(self):
        """this is for a proactive call from client: Asks user if she/he wants to start coooking now.

        Returns:
            response (dict): the response including speaking text, html, context and follow_up usecase (cooking)
        """

        response = {
            "text": "Hey, have you already cooked? If not, would you like to cook now?",
            "html": "<p>Hey, have you already cooked? If not, would you like to cook now?</p>",
            "follow_up": "cooking",
            "context": "cook"
        }

        return response

    def cookNow(self, text, preferences):
        """This method is vfor immediate cooking or for answer handling of method "askForCooking". \
            It looks for a planned meal and provide a receipe anyway.
            Moeover it asks for a playlist suggestion

        Args:
            text (string): spoken text from the user
            preferences (dict): all user preferences, which are collected over the frontend

        Returns:
            response (dict): the response including speaking text, html, context and follow_up usecase (cooking)
        """

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
                recipe = recipe_engine.get_recipe_by_ingredients(
                    meal, False, diet, health)

                text = "Today you haven't planned anything to eat. But I found a recipe for " + \
                    recipe["recipe_name"] + \
                    ". Would you like to listen to some music?"

            else:
                # get a random recipe
                diet = preferences.get("diet", "balanced")
                health = preferences.get("health", None)
                ingredients = ['rice', 'potato', 'chicken', 'noodles']
                recipe = recipe_engine.get_recipe_by_ingredients(
                    random.choice(ingredients), False, diet, health)

                text = "Today you have planned " + \
                    recipe["recipe_name"] + \
                    ". Would you like to listen to some music?"

            # write ingredients to shopping list
            ingredients_list = recipe["recipe_ingredients"]
            google_tasks = Tasks()
            today = datetime.date.today()
            for ingredient in ingredients_list:
                google_tasks.add_task_to_list(
                    "shoppingList"+str(today), ingredient)

            # build response
            html = html_builder.img_title_subtitle(
                text="Here is your recipe. Would you like to listen to some music?",
                title=recipe["recipe_name"],
                subtitle=str(int(recipe["recipe_time"]))+" min, " +
                str(recipe["recipe_calories"]) + " calories",
                image_url=recipe["recipe_image"],
                link=recipe["recipe_url"]
            )

            response = {
                "text": text,
                "html": html,
                "follow_up": "cooking",
                "context": "spotify"
            }

        return response
