from flask import Flask
from flask import render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/gallery")
def gallery():
    # create dynamic image grid + lightbox in the future
    return render_template('gallery.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/services/decks")
def decks():
    return render_template('decks.html')

@app.route("/services/interior")
def interior():
    return render_template('interior.html')

@app.route("/services/exterior")
def exterior():
    return render_template('exterior.html')

@app.route("/services/electrical")
def electrical():
    return render_template('electrical.html')

@app.route("/services/plumbing")
def plumbing():
    return render_template('plumbing.html')

@app.route("/services/stonework")
def stonework():
    return render_template('stonework.html')



