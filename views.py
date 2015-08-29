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
	guess = int(math.floor((min + max) / 2))

	lowerLink = '/guess/{min}/{max}/{count}'.format(min = min, max = (guess-1), count = count+1)
	higherLink = '/guess/{min}/{max}/{count}'.format(min = (guess+1), max = max, count = count+1)
	successLink = '/success/{count}'.format(count = count)

	if min > max:
		return render_template('error.html')

	return render_template('guess.html', guess = guess, lowerLink = lowerLink, higherLink = higherLink, successLink = successLink)

@app.route('/success/<int:count>')
def success(count):
	return render_template('success.html', count = count)