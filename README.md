# personal-assistant

## Run Server

1. `pip install Django`

2. `pip install django-cors-headers`

3. Start Server `python3 assistant/manage.py runserver`

4. Open [localhost:8000](http://localhost:8000/)

## UI Elements

### News

```html
<p>Good Morning!<br> today it's going to be sunny 22 degrees. NASA's "Perseverance" rover has successfully touched down on Mars. For more information check this website:</p>
<div class="img-title-subtitle">
    <div class="image">
        <img src="https://kodi.tv/sites/default/files/styles/medium_crop/public/addon_assets/plugin.video.nytimes/icon/icon.png?itok=W4Q-1JCU" alt="NYT">
    </div>
    <div class="title">
        <a class="title" href="https://www.tagesschau.de/ausland/mars-landung-101.html">Rover "Perseverance" lands on Mars</a>
    </div>
    <div class="subtitle">
        <a>by New York Times</a>
    </div>
</div>
```

### Lecture

```html
<p>Your next lecture "Semantic Web" starts in 10 minutes. Remember your "exam questions" assignment. Here is the Zoom link:</p>
<div class="time-title-subtitle">
    <div class="time">
        <a>14:00<br> 16:00</a>
    </div>
    <div class="title">
        <a class="title" href="https://dhbw-stuttgart.zoom.us/j/2334403821?pwd=RWpkUjFQSnlZdVEwRDNLTWV0QS9tQT09">Semantic Web</a>
    </div>
    <div class="subtitle">
        <a>Zoom Meeting</a>
    </div>
</div>
```

### Train departures

```html
<p>Hier sind deine nächsten Bahn-Abfahren:</p>
<div class="list-time-title">
    <div class="time">
        12:57
    </div>
    <div class="train">
        S1 Herrenberg
    </div>
    <div class="plate">
        Gleis 1
    </div>
</div>
<div class="list-time-title">
    <div class="time">
        13:02
    </div>
    <div class="train">
        S1 Kirchheim
    </div>
    <div class="plate">
        Gleis 2
    </div>
</div>
<div class="list-time-title">
    <div class="time">
        13:13
    </div>
    <div class="train">
        S1 Böblingen
    </div>
    <div class="plate">
        Gleis 1
    </div>
</div>
```

### Spotify playlist

```html
<p>Alright, do you want me to start the playlist?</p>
<div class="img-title-subtitle">
    <div class="image">
        <img src="https://i.scdn.co/image/ab67706c0000bebb962c73acdda7a8a9d07a523c" alt="Playlist">
    </div>
    <div class="title">
        <a class="title" href="https://open.spotify.com/playlist/2237sMNMlXS4wWLgdQ1UuV">Workout Motivation 2020💪</a>
    </div>
    <div class="subtitle">
        <a>by Jay Culter</a>
    </div>
</div>
```

### Bundesliga table

```html
<p>Borussia Dortmund lost 4:2 against FC Bayern Munich. Bayern remains at the top of the table:</p>
<div class="rank-image-name">
    <div class="place">
        <a>1</a>
    </div>
    <div class="image">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/Logo_FC_Bayern_M%C3%BCnchen_%282002%E2%80%932017%29.svg/240px-Logo_FC_Bayern_M%C3%BCnchen_%282002%E2%80%932017%29.svg.png" alt="Logo">
    </div>
    <div class="name">
        Bayern
    </div>
</div>
<div class="rank-image-name">
    <div class="place">
        <a>2</a>
    </div>
    <div class="image">
        <img src="https://upload.wikimedia.org/wikipedia/en/thumb/0/04/RB_Leipzig_2014_logo.svg/800px-RB_Leipzig_2014_logo.svg.png" alt="Logo">
    </div>
    <div class="name">
        Leipzig
    </div>
</div>
<div class="rank-image-name">
    <div class="place">
        <a>3</a>
    </div>
    <div class="image">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/Logo-VfL-Wolfsburg.svg/1024px-Logo-VfL-Wolfsburg.svg.png" alt="Logo">
    </div>
    <div class="name">
        Wolfsburg
    </div>
</div>
```