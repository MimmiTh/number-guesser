from app import app
from flask import request
import math

@app.route('/')
@app.route('/index')
def index():
	min = 0 if request.args.get('min') is None else request.args.get('min')
	max = 100 if request.args.get('max') is None else request.args.get('max')
	count = 1 if request.args.get('count') is None else request.args.get('count')+1

	guess = int(math.floor((min + max) / 2))

	lowerLink = '/?min={min}&max={max}&count={count}'.format(min = min, max = (guess+1), count = count)
	higherLink = '/?min={min}&max={max}&count={count}'.format(min = (guess-1), max = max, count = count)
	successLink = '/success?count={count}'.format(count = count)