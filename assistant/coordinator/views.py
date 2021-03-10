from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from usecases.welcome import Welcome
from usecases.meeting import Meeting
from usecases.cooking import Cooking
from usecases.evening import Evening

from wrapper.google_calendar import Calendar
from datetime import datetime, timedelta

@csrf_exempt
def index(request):
    if request.method == "POST":
        text = request.POST['text']
        text = text.lower()
        
        keywords_welcome = ["welcome", "morning", "hello", "hi"]
        keywords_meeting = ["meeting", "appointment"]
        keywords_cooking = ["food", "eat", "lunch", "dinner", "hungry"]
        keywords_evening = ["night", "sleep"]

        if any(keyword in text for keyword in keywords_welcome):

            welcome = Welcome()            
            response = welcome.handle(text, None, None)

            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_meeting):
            
            meeting = Meeting()            
            response = meeting.handle(text, None, None)

            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_cooking):
            
            cooking = Cooking()            
            response = cooking.handle(text, None, None)

            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_evening):
            
            evening = Evening()            
            response = evening.handle(text, None, None)

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
        now = datetime.now() + timedelta(hours = 1)

        morning_default = datetime.strptime(request.POST['morning_reminder'],'%H:%M')
        shopping_default = datetime.strptime(request.POST['shopping_reminder'],'%H:%M')
        cooking_default = datetime.strptime(request.POST['cooking_reminder'],'%H:%M')
        evening_default = datetime.strptime(request.POST['evening_reminder'],'%H:%M')

        morning = now.replace(hour=morning_default.hour, minute=morning_default.minute)
        shopping = now.replace(hour=shopping_default.hour, minute=shopping_default.minute)
        cooking = now.replace(hour=cooking_default.hour, minute=cooking_default.minute)
        evening = now.replace(hour=evening_default.hour, minute=evening_default.minute)

        calendar = Calendar("DHBW6")
        todays_events = calendar.get_events_today()
        # [{'title': 'Interaktive Systeme', 'location': '', 'start': '14:00', 'end': '17:00'}]        

        for event in todays_events:
            _event_start = datetime.strptime(event['start'],'%H:%M') + timedelta(minutes = -10)

            event_start = now.replace(hour=_event_start.hour, minute=_event_start.minute)
            if now < event_start:
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