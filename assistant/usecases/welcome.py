class Welcome:

  def __init__(self):
    self.context = None

  def handle(self, text, context, preferences):
    if context == "workout":
      return self.workout(text, preferences)
    elif "spotify" in context:
      return self.spotify(text, preferences, context) #context is playlist_uri
    else:
      return self.welcome(text, preferences)

  def time_for_workout?(self, event):
    if event.size
      diff = datetime.strptime(event[0].start, '%H:%M') - datetime.now()
      if diff.total_seconds() < 3600: # One hour
        return False
    return True

  def welcome(self, text, preferences):
    greetings = "Good morning."

    weather = Weather.get_todays_forecast

    articleList = NewsScrapper.getArticleList
    news = articleList[0].description
    news_preview = HTMLResponseBuilder.img_title_subtitle(articleList[0].text, articleList[0].title, articleList[0].subtitle, articleList[0].image_url, articleList[0].link)

    events = Calendar.get_events_for_today
    if events.size:
      calendar = "Today you have no entries in your calendar."
    else:
      calendar = "Today you have " + str(events.size) + " lectures. The first starts at "+events[0].start + "."


    text = greetings + " " + weather + " " + news + " " + calendar
    html = "<p>" + greetings + " " + weather + " " + news + "</p>" + news_preview + "<p>" + calendar + "</p>"
    if self.time_for_workout?(events):
      text += " Do you want to start a workout an listen to some music?"
      html += "<p>Do you want to start a workout an listen to some music?</p>"
      follow_up = "welcome"
      context = "workout"
    else:
      follow_up = None
      context = None

    return { "text": text, "html": html, "follow_up": follow_up, "context": context }

  def workout(self, text, preferences):
    if text.lower.find(positive_text) >= 0:
      answer = "<p>Ok. Should I start the playlist on Spotify?</p>"
      spt = Spotify.get_playlist("workout")[0]
      spotify_preview = HTMLResponesBuilder.img_title_subtitle(spt.text, spt.title, spt.author, spt.image_url, spt.uri)
      return { "text": answer, "html": answer + spotify_preview, "follow_up": "welcome", "context": spt.uri }
    else:
      return { "text": None, "html": None, "follow_up": None, "context": None }


  def spotify(self, text, preferences, playback_uri):
    positive_text = ['yes', 'ok']
    if text.lower.find(positive_text) >= 0:
      Spotfiy.start_playback(playback_uri)
    return { "text": None, "html": None, "follow_up": None, "context": None }
