from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from usecases.welcome import Welcome
from usecases.meeting import Meeting
from usecases.cooking import Cooking
from usecases.evening import Evening

from wrapper.google_calendar import Calendar
from datetime import datetime, timedelta

import pytz
import json

@csrf_exempt
def index(request):
    if request.method == "POST":

        #print(request.POST)

        text = request.POST['text'].lower()
        follow_up = request.POST['follow_up']
        context = request.POST['context']
        preferences = request.POST['preferences']
        print("preferences views.index:")
        print(type(preferences))
        print(preferences)
        welcome = Welcome()
        meeting = Meeting()
        cooking = Cooking()
        evening = Evening()

        preferences = json.loads(preferences)

        if follow_up == "welcome":
            response = welcome.handle(text, context, preferences)
            return JsonResponse(response)
        
        elif follow_up == "meeting":
            response = meeting.handle(text, context, preferences)
            return JsonResponse(response)

        elif follow_up == "cooking":
            response = cooking.handle(text, context, preferences)
            return JsonResponse(response)

        elif follow_up == "evening":
            response = evening.handle(text, context, preferences)
            return JsonResponse(response)

        else:

            keywords_welcome = ["welcome", "morning", "hello", "hi"]
            keywords_meeting = ["meeting", "appointment"]
            keywords_cooking = ["food", "eat", "lunch", "dinner", "hungry"]
            keywords_evening = ["night", "sleep"]

            if any(keyword in text for keyword in keywords_welcome):

                response = welcome.handle(text, context, preferences)

                return JsonResponse(response)

            elif any(keyword in text for keyword in keywords_meeting):

                response = meeting.handle(text, context, preferences)

                return JsonResponse(response)

            elif any(keyword in text for keyword in keywords_cooking):

                response = cooking.handle(text, context, preferences)

                return JsonResponse(response)

            elif any(keyword in text for keyword in keywords_evening):

                response = evening.handle(text, context, preferences)

                return JsonResponse(response)

            else:
                response = {
                    "text": "Sorry, I did not understand that",
                    "html": "<p>Sorry, I did not understand that<p>",
                    "follow_up": None,
                    "context": None
                }
                return JsonResponse(response)

    else:
        return HttpResponse("Coordinator: Please POST data")

@csrf_exempt
def reminder(request):
    if request.method == "POST":
        
        reminders = []

        timzone_berlin = pytz.timezone('Europe/Berlin')
        now = datetime.now(timzone_berlin)

        morning_default = datetime.strptime(request.POST['morning_reminder'],'%H:%M')
        shopping_default = datetime.strptime(request.POST['shopping_reminder'],'%H:%M')
        cooking_default = datetime.strptime(request.POST['cooking_reminder'],'%H:%M')
        evening_default = datetime.strptime(request.POST['evening_reminder'],'%H:%M')

        morning = now.replace(hour=morning_default.hour, minute=morning_default.minute)
        shopping = now.replace(hour=shopping_default.hour, minute=shopping_default.minute)
        cooking = now.replace(hour=cooking_default.hour, minute=cooking_default.minute)
        evening = now.replace(hour=evening_default.hour, minute=evening_default.minute)

        calendar = Calendar("ASWE")
        todays_events = calendar.get_events_today()      

        for event in todays_events:
            event_start = datetime.strptime(event['start'],'%H:%M') + timedelta(minutes = -10)
            event_start = now.replace(hour=event_start.hour, minute=event_start.minute)
            reminders.append({"ts": event_start.strftime("%H:%M"), "hour": event_start.hour, "minute": event_start.minute, "usecase": "meeting"})
        
        if now < morning:
            reminders.append({"ts": morning.strftime("%H:%M"), "hour": morning.hour, "minute": morning.minute, "usecase": "welcome"})
        
        if now < shopping:
            reminders.append({"ts": shopping.strftime("%H:%M"), "hour": shopping.hour, "minute": shopping.minute, "usecase": "hungry"})
        
        if now < cooking:
            reminders.append({"ts": cooking.strftime("%H:%M"), "hour": cooking.hour, "minute": cooking.minute, "usecase": "hungry"})
        
        if now < evening:
            reminders.append({"ts": evening.strftime("%H:%M"), "hour": evening.hour, "minute": evening.minute, "usecase": "night"})

        reminders = sorted(reminders, key=lambda k: k['ts'])

        return JsonResponse({"reminders": reminders})

    else:
        return HttpResponse("Reminder: Please POST data")