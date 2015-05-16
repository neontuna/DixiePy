from flask import Flask, render_template
from pw import *

app = Flask(__name__)

@app.route('/')
def myIndex():
	passwordList = makeGoodPass()
	return render_template('index.html', passwordList = passwordList)
	##return '%s' % makeGoodPass()
	
if __name__ == "__main__":
	app.run()
