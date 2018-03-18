"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from sutudyMemo import app
from json import JSONDecoder
from urllib import *

@app.route('/')
def home():
    title = "LineTEXT"
    return render_template(
        'memo.html',
        title=title
        )

@app.route('/send')
def send():
    
