import random
import string

def file_to_word_list(path):

	with open(path, 'r') as f:
		contents = f.read()
		contents = contents.replace(".", "").replace(",","").replace("*", "").replace(string.punctuation, "").replace("?", "").replace("!", "").replace(";", "").replace(":", "").replace("-", "")
		contents = contents.lower()

	return contents.split()

def sentence_to_word_list(sentence):
	return sentence.lower().split()

def first_markov_chain(listt):
	'''Reads from a sentence and returns a ditcionary with:
	(key) as the keys/words in the sentence
	(value) as a dictionary containg words that come after the (key)
	'''

	markov = {}

	# appending | key: unique words in sentence, value: empty dictionary | into {markov}
	for item in listt:
		if item not in markov:
			markov[item] = {}

	# indexing through items in the markov chain
	for index in range(0, (len(listt) - 1)):
		curr_word = listt[index]
		next_word = listt[index + 1]

		value = markov[curr_word]

		if next_word in value:		# add count of occurences by 1
			value[next_word] += 1
		else:
			value[next_word] = 1	# set count of occurences to 1
	return markov


def generate_sentence(first_mark):
	final_list = []
	times = 0

	curr_word = random.choice(list(first_mark.keys()))	# gets first item in dictionary

	while times < 15:

		final_list.append(curr_word)
		dict_of_next_words = first_mark[curr_word]


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

	return " ".join(final_list)




if __name__ == "__main__":
	sent = 'One fish two fish red fish blue fish'
	word_array = sentence_to_word_list(sent)
	mark = first_markov_chain(word_array)
	# print(mark)
	# print(generate_sentence(mark))

	# new_sent = 'Hi my name is Rinni my bestfriend is Sarin and we love each other so much'
	# new_word_array = sentence_to_word_list(new_sent)
	# print(first_markov_chain(new_word_array))

	neww_sent = 'I like cats and you like cats I like dogs but you hate dogs'
	neww_word_array = sentence_to_word_list(neww_sent)
	markk = first_markov_chain(neww_word_array)
	# print(generate_sentence(markk))


	lis = file_to_word_list('BreakfastAtTiffanys.txt')
	markkk = first_markov_chain(lis)
	print(markkk)
	print(generate_sentence(markkk))

	



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