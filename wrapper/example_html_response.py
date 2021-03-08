from html_response import HTMLResponseBuilder
builder = HTMLResponseBuilder()

departures = [
        {
            "time": "14:07", 
            "train": "S1 Herrenberg", 
            "plate": "Plate 1"
        },
        {
            "time": "14:12", 
            "train": "S1 Plochingen", 
            "plate": "Plate 2"
        }
    ]

html = builder.bahn(text="Here are the next departures", departures=departures)

print(html)