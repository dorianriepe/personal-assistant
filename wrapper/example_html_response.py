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

table = [
    {
        "rank": 1,
        "clubShortName": "Bayern",
        "teamID": 40,
        "points": 49,
        "teamIconUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Logo_FC_Bayern_M%C3%BCnchen_%282002%E2%80%932017%29.svg/240px-Logo_FC_Bayern_M%C3%BCnchen_%282002%E2%80%932017%29.svg.png"
    },
    {
        "rank": 2,
        "clubShortName": "Leipzig",
        "teamID": 1635,
        "points": 47,
        "teamIconUrl": "https://upload.wikimedia.org/wikipedia/en/thumb/0/04/RB_Leipzig_2014_logo.svg/800px-RB_Leipzig_2014_logo.svg.png"
    },
    {
        "rank": 3,
        "clubShortName": "Wolfsburg",
        "teamID": 131,
        "points": 42,
        "teamIconUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Logo-VfL-Wolfsburg.svg/1024px-Logo-VfL-Wolfsburg.svg.png"
    },
    {
        "rank": 4,
        "clubShortName": "Frankfurt",
        "teamID": 91,
        "points": 42,
        "teamIconUrl": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Eintracht_Frankfurt_Logo.svg/1024px-Eintracht_Frankfurt_Logo.svg.png"
    },
    {
        "rank": 5,
        "clubShortName": "Leverkusen",
        "teamID": 6,
        "points": 37,
        "teamIconUrl": "https://upload.wikimedia.org/wikipedia/de/thumb/f/f7/Bayer_Leverkusen_Logo.svg/1280px-Bayer_Leverkusen_Logo.svg.png"
    }
]

text="today it's going to be sunny 22 degrees. NASA's Perseverance rover has successfully touched down on Mars. For more information check this website"
title="Rover Perseverance lands on Mars"
subtitle="by New York Times"
image_url="https://kodi.tv/sites/default/files/styles/medium_crop/public/addon_assets/plugin.video.nytimes/icon/icon.png?itok=W4Q-1JCU"
link="https://www.tagesschau.de/ausland/mars-landung-101.html"
html = builder.img_title_subtitle(text, title, subtitle, image_url, link)
print(html)
print("###")

text="Your next lecture Semantic Web starts in 10 minutes. Remember your exam questions assignment. Here is the Zoom link:"
title="Semantic Web"
subtitle="Zoom Meeting"
from_time="14:00"
to_time="16:00"
link="https://dhbw-stuttgart.zoom.us/j/2334403821?pwd=RWpkUjFQSnlZdVEwRDNLTWV0QS9tQT09"
html = builder.time_title_subtitle(text, title, subtitle, from_time, to_time, link)
print(html)
print("###")

html = builder.list_time_title(text="Here are the next departures", departures=departures)
print(html)
print("###")

text="Borussia Dortmund lost 4:2 against FC Bayern Munich. Bayern remains at the top of the table:"
html = builder.rank_image_name(text, table)
print(html)
print("###")