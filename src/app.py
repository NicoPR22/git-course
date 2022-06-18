from asyncio import run_coroutine_threadsafe
from unicodedata import name
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello!'

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    sum_nums = a + b
    return f"La suma es: {str(sum_nums)}"

