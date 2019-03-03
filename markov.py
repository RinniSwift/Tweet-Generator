import random

def file_to_word_list(path):

	with open(path, 'r') as f:
		contents = f.read()
		contents = contents.replace(".", "").replace(",","").replace("*", "").replace(string.punctuation, "").replace("?", "").replace("!", "").replace(";", "").replace(":", "")

	return contents.split()

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
	 'fish': {'two': 1, 'red': 1, 'blue': 1}, 
	 'two': {'fish': 1}, 
	 'red': {'fish': 1}, 
	 'blue': {'fish': 1}
	 }
	'''

	'''
	{'Hi': {'my': 1}, 
	 'my': {'name': 1, 'bestfriend': 1}, 
	 'name': {'is': 1}, 
	 'is': {'Rinni': 1, 'Sarin': 1}, 
	 'Rinni': {'my': 1}, 
	 'bestfriend': {'is': 1}, 
	 'Sarin': {'and': 1}, 
	 'and': {'we': 1}, 
	 'we': {'love': 1}, 
	 'love': {'each': 1}, 
	 'each': {'other': 1}, 
	 'other': {'so': 1}, 
	 'so': {'much': 1}, 
	 'much': {}
	 }
	 '''

	'''
	 {'I': {'like': 2}, 
	  'like': {'cats': 2, 'dogs': 1}, 
	  'cats': {'and': 1, 'I': 1}, 
	  'and': {'you': 1}, 
	  'you': {'like': 1, 'hate': 1}, 
	  'dogs': {'but': 1}, 
	  'but': {'you': 1}, 
	  'hate': {'dogs': 1}}
	'''

def generate_sentence(first_mark):
	pass
	final_sent = ""
	times = 0

	curr_word = random.choice(list(first_mark.keys()))	# gets first item in dictionary

	while times < 5:

		final_sent += (curr_word + " ")
		dict_of_next_words = first_mark[curr_word]
		print(dict_of_next_words)


		if len(dict_of_next_words) == 1:
			curr_word = list(dict_of_next_words.keys())[0]

		elif len(dict_of_next_words) > 1:
			# sample word choice
			count = 0
			random_number = random.random()
			for key, value in dict_of_next_words.items():
				count += (value / len(dict_of_next_words))
				if count >= random_number:
					curr_word = key

		elif len(dict_of_next_words) == 0:
			curr_word = random.choice(list(first_mark.keys()))

		times += 1

	print("final sentence: {}".format(final_sent))




if __name__ == "__main__":
	sent = 'one fish two fish red fish blue fish'
	word_array = sentence_to_word_list(sent)
	mark = first_markov_chain(word_array)
	print(mark)
	generate_sentence(mark)

	# new_sent = 'Hi my name is Rinni my bestfriend is Sarin and we love each other so much'
	# new_word_array = sentence_to_word_list(new_sent)
	# print(first_markov_chain(new_word_array))

	neww_sent = 'I like cats and you like cats I like dogs but you hate dogs'
	neww_word_array = sentence_to_word_list(neww_sent)
	markk = first_markov_chain(neww_word_array)
	generate_sentence(markk)

	



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