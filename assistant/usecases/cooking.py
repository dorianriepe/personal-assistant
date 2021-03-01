class Cooking:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):
        
        response = {
                "text": "Today you have planned spaghetti with tomato sauce. You don't have any appointments between 12am and 2pm. Shall I put the ingredients on the shopping list?",
                "html": "<p>Today you have planned spaghetti with tomato sauce. You don't have any appointments between 12:00 and 14:00. Shall I put the ingredients on the shopping list?<p>",
                "follow_up": "cooking",
                "context": "test"
            }

        return response