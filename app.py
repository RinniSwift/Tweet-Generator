from flask import Flask

import markov
import string

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!' 

@app.route('/')
def hello_world():
	file_split = markov.file_to_word_list('BreakfastAtTiffanys.txt')
	dictionary = markov.first_markov_chain(file_split)
	return markov.generate_sentence(dictionary)
	
