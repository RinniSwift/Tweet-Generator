
def sentence_to_word_list(sentence):
	return sentence.split()

def first_markov_chain(listt):
	'''Reads from a sentence and returns a ditcionary with:
	(key) as the keys/words in the sentence
	(value) as a dictionary containg words that come after the (key)
	'''
	'''listt: one fish two fish red fish blue fish'''

	markov = {}

	# appending | key: unique words in sentence, value: empty dictionary | into {markov}
	for item in listt:
		if item not in markov:
			markov[item] = {}


	index = 0
	while index <= len(listt) - 2:	# indexing all indexes before the last index
		curr_word = listt[index]
		next_word = listt[index + 1]

		for word_pair in markov.items():
			if curr_word == word_pair[0]:	# check if curr_word in dictionaries key
				value = word_pair[1]		# set value variable to the dictionaries value at that key
				if next_word in value:
					value[next_word] += 1	# word has come after that key before, increment its count by 1
				else:
					value[next_word] = 1	# word has not come after that key, store the count of 1
		index += 1
	return markov
	'''
	{'one': {'fish': 1}, 
	 'fish': {'two': 1, 
	 'red': 1, 'blue': 1}, 
	 'two': {'fish': 1}, 
	 'red': {'fish': 1}, 
	 'blue': {'fish': 1}
	 }
	'''

if __name__ == "__main__":
	sent = 'one fish two fish red fish blue fish'
	word_array = sentence_to_word_list(sent)
	first_markov_chain(word_array)



'''
second markov chain

{	'one fish': {'two': 1}, 
	'fish two': {'fish': 1}, 
	'two fish': {'red': 1}, 
	'fish red': {'fish': 1}, 
	'red fish': {'fish': 1},
	'fish blue': {'fish': 1},
	'blue fish': {}
}

'''