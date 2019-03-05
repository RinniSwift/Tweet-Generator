from flask import Flask

import markov

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!' 
app.file_split = markov.file_to_word_list('corpus.txt')
app.dictionary = markov.first_markov_chain(app.file_split)
@app.route('/')
def hello_world():
	return markov.generate_sentence(app.dictionary)
