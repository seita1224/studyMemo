from flask import Flask

app = Flask(__name__)
from studyMemo.views import views
from studyMemo.views import api
