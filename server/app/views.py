from app import app
from flask import render_template, request


@app.route('/', methods=['GET'])
def home():
    return "Hello World!"