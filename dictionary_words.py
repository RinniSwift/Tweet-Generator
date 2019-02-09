'''
* read in the words file '/usr/share/dict/words'
* select a random set of words from the file and store in a data type
* put the number of words requested together into a "sentence"
* output your sentence'''

import sys
import random

def generate_sentence_from_dict(file):
	# get the number of words passed in as the terminal input
	word_count = sys.argv[1]

	# use the 'with' keyword to make sure you close the file after
	with open(file, 'r') as f:							
		file_content = f.read()			
	lines = file_content.split()

	words = random.choices(lines, k=int(word_count))

	return " ".join(words)


def sentence_form(string):
	return string.capitalize() + "."


if __name__ == "__main__":
	generate_words = generate_sentence_from_dict('/usr/share/dict/words')
	print(sentence_form(generate_words))


