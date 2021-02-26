from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "POST":
        text = request.POST['text']
        text = text.lower()
        
        keywords_welcome = ["willkommen", "morgen", "hallo", "guten tag", "moin", "hi"]
        keywords_meeting = ["meeting", "termin"]
        keywords_cooking = ["kochen", "essen", "mittag", "hunger"]
        keywords_evening = ["schlaf", "nacht"]

        if any(keyword in text for keyword in keywords_welcome):
            response = {
                "text": "Guten Morgen, heute werden es 22 Grad und es wird sonnig. Dem NASA Rover Perseverance ist die Mars Landung gelungen.",
                "html": "<p>Guten Morgen!<br> heute werden es 22°C und sonnig. NASA-Rover \"Perseverance\" gelingt Mars-Landung. Mehr Infos findest du hier:<p><a href=\"https://www.tagesschau.de/ausland/mars-landung-101.html\">Perservance gelingt Mars Landung</a>",
                "follow_up": "welcome",
                "context": "test"
            }
            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_meeting):
            response = {
                "text": "Deine nächste Vorlesung Semantic Web startet in 10 Minuten. Denk an deine Fragen zur Prüfungsleistung.",
                "html": "<p>Deine nächste Vorlesung \"Semantic Web\" startet in 10 Minuten. Denk an die Aufgabe \"Fragen zur Prüfungsleistung\". Hier ist der Link zur Vorlesung:<p><a href=\"https://dhbw-stuttgart.zoom.us/j/2334403821?pwd=RWpkUjFQSnlZdVEwRDNLTWV0QS9tQT09\">Semantic Web</a>",
                "follow_up": "meeting",
                "context": "test"
            }
            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_cooking):
            response = {
                "text": "Heute hast du Spagetti Tomatensauce geplant. Du hast zwischen 12:00 und 14:00 Uhr keine Termine. Soll ich dir die Zutaten auf die Einkaufsliste setzten?",
                "html": "<p>Heute hast du Spagetti Tomatensauce geplant. Du hast zwischen 12:00 und 14:00 Uhr keine Termine. Soll ich dir die Zutaten auf die Einkaufsliste setzten?<p>",
                "follow_up": "cooking",
                "context": "test"
            }
            return JsonResponse(response)

        elif any(keyword in text for keyword in keywords_evening):
            response = {
                "text": "Guten Abend, dein erster Termin morgen ist um 8 Uhr. Wenn du 9 Stunden Schlaf bekommen möchtest geh demnächst schlafen.",
                "html": "<p>Guten Abend, <br> dein erster Termin morgen ist um 8 Uhr. Wenn du 9 Stunden Schlaf bekommen möchtest geh demnächst schlafen.<p>",
                "follow_up": "evening",
                "context": "test"
            }
            return JsonResponse(response)
        
        else:
            response = {
                "text": "Das habe ich leider nicht verstanden",
                "html": "<p>Das habe ich leider nicht verstanden<p>",
                "follow_up": None,
                "context": None
            }
            return JsonResponse(response)

    else:
        return HttpResponse("Please POST")
