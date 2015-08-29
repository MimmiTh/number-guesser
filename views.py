from app import app
from flask import request
from flask import render_template
import math

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/guess')
def guess():
	min = 0 if request.args.get('min') is None else int(request.args.get('min'))
	max = 100 if request.args.get('max') is None else int(request.args.get('max'))
	count = 1 if request.args.get('count') is None else int(request.args.get('count'))+1

	guess = int(math.floor((min + max) / 2))

	lowerLink = '/guess?min={min}&max={max}&count={count}'.format(min = min, max = (guess-1), count = count)
	higherLink = '/guess?min={min}&max={max}&count={count}'.format(min = (guess+1), max = max, count = count)
	successLink = '/success?count={count}'.format(count = count)

	return render_template('guess.html', guess = guess, lowerLink = lowerLink, higherLink = higherLink, successLink = successLink)

@app.route('/success')
def success():
	return render_template('success.html', count = count)