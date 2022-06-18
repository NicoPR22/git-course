from asyncio import run_coroutine_threadsafe
from unicodedata import name
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

