
def sentence_to_word_list(sentence):
	return sentence.split()


def markov_chain(listt):
	markov = {}
	types = 0

	for item in listt:
		if item not in markov:
			markov[item] = {}

	index = 0
	while index <= len(listt) - 2:
		curr_word = listt[index]
		next_word = listt[index + 1]

		for word_pair in markov.items():
			if curr_word == word_pair[0]:
				value = word_pair[1]
				if next_word in value:
					value[next_word] += 1
				else:
					value[next_word] = 1
		index += 1
	print(markov)


if __name__ == "__main__":
	sent = 'one fish two fish red fish blue fish'
	word_array = sentence_to_word_list(sent)
	markov_chain(word_array)