class Evening:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):
        
        response = {
                "text": "Good evening, Borussia Dortmund lost 4:2 against FC Bayern Munich. Bayern remains at the top of the table",
                "html": "<p>Borussia Dortmund lost 4:2 against FC Bayern Munich. Bayern remains at the top of the table:</p><div class=\"rank-image-name\"><div class=\"place\"><a>1</a></div><div class=\"image\"><img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Logo_FC_Bayern_M%C3%BCnchen_%282002%E2%80%932017%29.svg/240px-Logo_FC_Bayern_M%C3%BCnchen_%282002%E2%80%932017%29.svg.png\" alt=\"Logo\"></div><div class=\"name\">Bayern</div></div><div class=\"rank-image-name\"><div class=\"place\"><a>2</a></div><div class=\"image\"><img src=\"https://upload.wikimedia.org/wikipedia/en/thumb/0/04/RB_Leipzig_2014_logo.svg/800px-RB_Leipzig_2014_logo.svg.png\" alt=\"Logo\"></div><div class=\"name\">Leipzig</div></div><div class=\"rank-image-name\"><div class=\"place\"><a>3</a></div><div class=\"image\"><img src=\"https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Logo-VfL-Wolfsburg.svg/1024px-Logo-VfL-Wolfsburg.svg.png\" alt=\"Logo\"></div><div class=\"name\">Wolfsburg</div></div>",
                "follow_up": "evening",
                "context": "test"
            }

        return response