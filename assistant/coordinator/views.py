from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from usecases.welcome import Welcome
from usecases.meeting import Meeting
from usecases.cooking import Cooking
from usecases.evening import Evening

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
        return HttpResponse("Please POST")
