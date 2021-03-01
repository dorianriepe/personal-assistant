class Welcome:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):
        
        response = {
                "text": "Good morning, today it's going to be sunny 22 degrees. NASA's Perseverance rover has successfully touched down on Mars.",
                "html": "<p>Good Morning!<br> today it's going to be sunny 22 degrees. NASA's \"Perseverance\" rover has successfully touched down on Mars. For more information check this website:<p><a href=\"https://www.tagesschau.de/ausland/mars-landung-101.html\">Rover \"Perseverance\" lands on Mars</a>",
                "follow_up": "welcome",
                "context": "test"
            }

        return response
        