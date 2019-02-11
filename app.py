from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!' 


@app.route('/favicon.ico')
def hello_something():
	return 'Hello something'