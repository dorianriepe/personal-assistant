from datetime import datetime
from wrapper.weather import Weather
from wrapper.news import NewsScraper
from wrapper.html_response import HTMLResponseBuilder
from wrapper.google_calendar import Calendar
from wrapper.spotify import Spotify

import json

class Welcome:

  def __init__(self):
    self.context = None

  def handle(self, text, context, preferences):
    
    preferences = json.loads(preferences)

    if context == None:
      return self.welcome(text, preferences)
    elif context == "workout":
      return self.workout(text, preferences)
    elif "spotify" in context:
      return self.spotify(text, preferences, context)
    else:
      return self.welcome(text, preferences)

  def time_for_workout(self, event):
    if len(event):
      diff = datetime.strptime(event[0]["start"], '%H:%M') - datetime.now()
      if diff.total_seconds() < 3600: # One hour
        return False
    return True

  def welcome(self, text, preferences):

    text = ""

    # Get greetings from preferences
    name = preferences["name"]
    text += "Good morning "+name+", "

    # Get Weather
    location = preferences["location"]
    w = Weather(location)
    text += w.get_forecast()+" "
    
    # Get News
    newsScraper = NewsScraper.getInstance()
    articleList = newsScraper.getArticleList()
    newspaper_logo = "https://res-4.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco/v1491958734/bqp32una36b06hmbulla.png"
    text += articleList[0]["description"]+" "

    # Get Calendar Information
    calendar = Calendar("DHBW6")
    events = calendar.get_events_today()
    if len(events) == 0:
      text += "Today you have no more entries in your calendar. "
    else:
      text  += "Today you have " + str(len(events)) + " lectures. The next starts at "+events[0]["start"] + ". "

    # Check if Time for workout
    if self.time_for_workout(events):
      text += "Do you want to start a workout an listen to some music? "
      follow_up = "welcome"
      context = "workout"
    else:
      follow_up = None
      context = None

    # Build HTML Response
    html_response_builder = HTMLResponseBuilder()
    html = html_response_builder.img_title_subtitle(text, articleList[0]["title"], "by New York Times", newspaper_logo, articleList[0]["link"])

    return { "text": text, "html": html, "follow_up": follow_up, "context": context }

  def workout(self, text, preferences):
    
    positive_text = ['yes', 'ok']

    if any(t in text for t in positive_text):

      text = "Ok. Should I start the playlist on Spotify?"
      
      spotify = Spotify()
      spt = spotify.get_playlist("workout")[0]
      html_builder = HTMLResponseBuilder()
      html = html_builder.img_title_subtitle(text, spt["name"], "by "+spt["author"], spt["image_url"], spt["uri"])
      
      return { "text": text, "html": html, "follow_up": "welcome", "context": spt["uri"] }

    else:
      return { "text": None, "html": None, "follow_up": None, "context": None }


  def spotify(self, text, preferences, playback_uri):
    
    positive_text = ['yes', 'ok']
    
    if any(t in text for t in positive_text):
      spotify = Spotify()
      spotify.start_playback(playback_uri)
    
    return { "text": None, "html": None, "follow_up": None, "context": None }
