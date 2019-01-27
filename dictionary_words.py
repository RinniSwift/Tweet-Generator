'''
* read in the words file '/usr/share/dict/words'
* select a random set of words from the file and store in a data type
* put the number of words requested together into a "sentence"
* output your sentence'''

import sys
import random

def generate_sentnce_from_dict(file):
	word_count = sys.argv[1]						# get the number of words passed in as the terminal input
	string = ""

	with open(file, 'r') as f:						# use the 'with' keyword to make sure you close the file after
		file_content = f.read()

	for i in range(0, int(word_count)):					# loop through n amount of times to add words to the string
		lines = file_content.split()					# split all words in the file
		random_line = random.randrange(0, len(lines))	# randomize a number from 0 to the length of the file word count
		string += (lines[random_line] + " ")			# append the files index to the string

	return string




if __name__ == "__main__":
	generate_words = generate_sentnce_from_dict('/usr/share/dict/words')
	print(generate_words)
