from flask import Flask
import markov

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!' 

@app.route('/')
def hello_world():
	return markov.generate_sentence(markov.first_markov_chain(markov.sentence_to_word_list(markov.read_file('/Users/rinniswift/dev/CS1.2/BreakfastAtTiffanys.txt'))))
