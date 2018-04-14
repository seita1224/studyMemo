"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import Flask
from studyMemo import app
from json import JSONDecoder
from urllib import *
from . import api

app = Flask(__name__)

api_connection = api('test','test','test','test')

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
    
