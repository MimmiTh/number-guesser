from app import app
from flask import request
from flask import render_template
import math

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/guess/<int:min>/<int:max>/<int:count>')
def guess(min, max, count):
	count+=1
	guess = int(math.floor((min + max) / 2))

	lowerLink = '/guess/{min}/{max}/{count}'.format(min = min, max = (guess-1), count = count)
	higherLink = '/guess/{min}/{max}/{count}'.format(min = (guess+1), max = max, count = count)
	successLink = '/success/{count}'.format(count = count)

	return render_template('guess.html', guess = guess, lowerLink = lowerLink, higherLink = higherLink, successLink = successLink)

@app.route('/success/<int:count>')
def success(count):
	return render_template('success.html', count = count)