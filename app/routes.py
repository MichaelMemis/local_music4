from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('main.html')


@app.route('/artists')
def artists():
    indexartist = ["Kurt Riley", "Little Feat", "Roben Trower", "Mark Cohn"]
    return render_template('artists.html', artists=indexartist)


@app.route('/artist')
def artist():
    artist = {"name": "Kurt Riley", "town": "Ithaca",
              "description": "Kurt Riley is an American rock and roll songwriter, performer, and musician. He knows "
                             "how to play a variety of instruments and enjoyed early rock and roll.",
              "listen": "Upcoming Events",
              "event1": "Saturday September 11 at Cornell University",
              "event2": "Monday September 13 at The Haunt"}

    return render_template('artist.html', artist=artist)


@app.route('/newartist')
def newartist():
    return render_template('newartist.html')
