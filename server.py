from flask import Flask
import numpy


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def dice(): 
    roll = numpy.random.randint(1,6) 
    return f"{roll}"