from flask import Flask
import numpy


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def dice(): 
    roll1 = numpy.random.randint(1,6)
    roll2 = numpy.random.randint(1,6) 
    roll3 = numpy.random.randint(1,6) 

    return f"{roll1}, {roll2}, {roll3}"