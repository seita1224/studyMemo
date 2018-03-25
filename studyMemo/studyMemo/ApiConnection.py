from ApiConnection import ApiConnection

import flask
from flask import (
    session, request, redirect, url_for, render_template_string, 
)
import oauth2 as oauth
'''
このクラスははてなブログに接続する際の処理を
ラップするためのクラスです。
'''
class ApiConnection():
    CONSUMER_KEY = None
    CONSUMER_SECRET = None
    SECRET_KEY = None
    SCOPE = None

    REQUEST_TOKEN_URL='https://www.hatena.com/oauth/initiate'
    ACCESS_TOKEN_URL='https://www.hatena.com/oauth/token'
    AUTHORIZE_URL='https://www.hatena.ne.jp/oauth/authorize'

    consumer = None
    
    def __init__(self ,CONSUMER_KEY,CONSUMER_SECRET,SECRET_KEY,SCOPE):
        '''
        インスタンス生成時にOAuthで使用するキー類の登録,スコープの指定を行う
        '''
        if CONSUMER_KEY is not None and not isinstance(CONSUMER_KEY, str):
            raise ValueError("Invalid CONSUMER_KEY.")

        if CONSUMER_SECRET is not None and not isinstance(CONSUMER_SECRET, str):
            raise ValueError("Invalid CONSUMER_SECRET.")

        if SECRET_KEY is not None and not isinstance(SECRET_KEY, str):
            raise ValueError("Invalid SECRET_KEY.")

        if SCOPE is not None and not isinstance(SCOPE, str):
            raise ValueError("Invalid SCOPE.")

        self.CONSUMER_KEY=CONSUMER_KEY
        self.CONSUMER_SECRET=CONSUMER_SECRET
        self.SECRET_KEY = SECRET_KEY
        self.SCOPE = SCOPE

        self.consumer = oauth.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
        
    def get_reqest_token(callback_url):
        # リクエストトークンの取得
        client = oauth.Client(consumer)
        resp, content = client.request('%s?scope=%s&oauth_callback=%s%s' % \
                (REQUEST_TOKEN_URL, SCOPE, request.url, callback_url))

    def get_accese_token():
        pass

    def request_form():
        pass
