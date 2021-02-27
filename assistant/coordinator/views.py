from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
            response = {
                "text": "Good morning, today it's going to be sunny 22 degrees. NASA's Perseverance rover has successfully touched down on Mars.",
                "html": "<p>Good Morning!<br> today it's going to be sunny 22 degrees. NASA's \"Perseverance\" rover has successfully touched down on Mars. For more information check this website:<p><a href=\"https://www.tagesschau.de/ausland/mars-landung-101.html\">Rover \"Perseverance\" lands on Mars</a>",
                "follow_up": "welcome",
                "context": "test"
            }
            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_meeting):
            response = {
                "text": "Your next lecture Semantic Web starts in 10 minutes. Remember your \"exam questions\" assignment.",
                "html": "<p>Your next lecture \"Semantic Web\" starts in 10 minutes. Remember your \"exam questions\" assignment. Here is the Zoom link:<p><a href=\"https://dhbw-stuttgart.zoom.us/j/2334403821?pwd=RWpkUjFQSnlZdVEwRDNLTWV0QS9tQT09\">Semantic Web</a>",
                "follow_up": "meeting",
                "context": "test"
            }
            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_cooking):
            response = {
                "text": "Today you have planned spaghetti with tomato sauce. You don't have any appointments between 12am and 2pm. Shall I put the ingredients on the shopping list?",
                "html": "<p>Today you have planned spaghetti with tomato sauce. You don't have any appointments between 12:00 and 14:00. Shall I put the ingredients on the shopping list?<p>",
                "follow_up": "cooking",
                "context": "test"
            }
            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_evening):
            response = {
                "text": "Good evening, your first appointment tomorrow is at 8. If you want to get 9 hours of sleep go to sleep soon.",
                "html": "<p>Good evening, <br>your first appointment tomorrow is at 8. If you want to get 9 hours of sleep go to sleep soon.<p>",
                "follow_up": "evening",
                "context": "test"
            }
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
        return HttpResponse("Please POST")
