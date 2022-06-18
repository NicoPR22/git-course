from asyncio import run_coroutine_threadsafe
from unicodedata import name
from unittest import result
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello!'

@app.route('/hello')
def greating():
    return 'Hello world!'

@app.route('/sum/<int:a>/<int:b>')
def sum(a: int, b: int):
    result = float(a * b)
    return result

@app.route('/mult/<int:a>/<int:b>')
def mult(a: int, b: int):
    result = float( a * b)
    return f"La multiplicacion es: {str(result)}"
