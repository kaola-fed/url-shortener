#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys, urllib, requests
from flask import Flask, request, render_template
app = Flask(__name__)

if len(sys.argv) < 2:
    sys.exit()

USERNAME = sys.argv[1]
BASE_URL = 'https://163.lu/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods = ['POST'])
def shorten():
    url = request.form['url']
    url = urllib.unquote(url.encode('utf-8'))
    params = {
        'user': USERNAME,
        'url': urllib.quote(url, safe = '~@#$&()*!+=:;,.?/\'')
    }
    res = requests.post('%sshorten/' % BASE_URL, params).json()

    return BASE_URL + res['hash']


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')