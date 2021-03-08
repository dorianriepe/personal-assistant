class Welcome:

    def __init__(self):
        self.context = None

    def handle(self, text, context, preferences):
        
        response = {
                "text": "Good morning, today it's going to be sunny 22 degrees. NASA's Perseverance rover has successfully touched down on Mars.",
                "html": "<p>Good Morning!<br> today it's going to be sunny 22 degrees. NASA's \"Perseverance\" rover has successfully touched down on Mars. For more information check this website:</p><div class=\"img-title-subtitle\"><div class=\"image\"><img src=\"https://kodi.tv/sites/default/files/styles/medium_crop/public/addon_assets/plugin.video.nytimes/icon/icon.png?itok=W4Q-1JCU\" alt=\"NYT\"></div><div class=\"title\"><a class=\"title\" href=\"https://www.tagesschau.de/ausland/mars-landung-101.html\">Rover \"Perseverance\" lands on Mars</a></div><div class=\"subtitle\"><a>by New York Times</a></div></div>",
                "follow_up": "welcome",
                "context": "test"
            }

        return response
        