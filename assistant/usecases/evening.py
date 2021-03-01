class Evening:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):
        
        response = {
                "text": "Good evening, your first appointment tomorrow is at 8. If you want to get 9 hours of sleep go to sleep soon.",
                "html": "<p>Good evening, <br>your first appointment tomorrow is at 8. If you want to get 9 hours of sleep go to sleep soon.<p>",
                "follow_up": "evening",
                "context": "test"
            }

        return response