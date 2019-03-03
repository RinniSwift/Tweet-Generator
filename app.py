from flask import Flask
import markov

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!' 

@app.route('/')
def hello_world():
	file_split = file_to_word_list('/Users/rinniswift/dev/CS1.2/BreakfastAtTiffanys.txt')
	dictionary = markov.first_markov_chain(file_split)
	return markov.generate_sentence(dictionary)
	
