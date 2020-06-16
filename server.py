from flask import Flask
import numpy


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/roll-dice')
def dice(): 
    roll1 = numpy.random.randint(1,7)
    roll2 = numpy.random.randint(1,7) 
    roll3 = numpy.random.randint(1,7) 

    return f"Let's see what you got!: {roll1}, {roll2}, {roll3}"