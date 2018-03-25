"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from studyMemo import app
from json import JSONDecoder
from urllib import *
from ApiConnection import *

apiConnection = ApiConnection('CONSUMER_KEY','CONSUMER_SECRET','SECRET_KEY','SCOPE')

@app.route('/')
def home():
    title = "LineTEXT"
    return render_template(
        'memo.html',
        title=title
        )

#フォームの値を送信するようメソッド
@app.route('/send')
def send():
    pass
    
