class Meeting:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):
        
        response = {
                "text": "Your next lecture Semantic Web starts in 10 minutes. Remember your \"exam questions\" assignment.",
                "html": "<p>Your next lecture \"Semantic Web\" starts in 10 minutes. Remember your \"exam questions\" assignment. Here is the Zoom link:<p><a class=\"online-meeting\" href=\"https://dhbw-stuttgart.zoom.us/j/2334403821?pwd=RWpkUjFQSnlZdVEwRDNLTWV0QS9tQT09\">Semantic Web</a>",
                "follow_up": "meeting",
                "context": "test"
            }

        return response