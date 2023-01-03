# We had to create this app.py file from scratch.
# This code will create a Flask app:
from flask import Flask, redirect, url_for, request, render_template, session
import requests, os, uuid, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    original_text = request.form['text']
    return render_template('results.html', original_text=original_text)