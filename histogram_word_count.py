from string import punctuation

def file_to_word_array(file):
	'''function that changes a text file to an array of words excluding all punctuations'''

	with open(file, 'r') as f:
		text_content = f.read()
	words = text_content.lower()
	word_arr_stripped = ''.join(c for c in words if c not in punctuation).split()
	return word_arr_stripped



def histogram_dict(words):
	'''returns a dictionary as the key being the type and the value being the tokens'''
	# DICTIONARY APPROACH O(n)

	histogram = {}

	for word in words:
		if word in histogram.keys():
			histogram[word] += 1
		else:
			histogram[word] = 1

	return histogram

def histogram_list_of_lists(words):
	'''returns a list of the words and amount of times it has appeared.'''
	# LIST APPROACH O(n^2)

	histogram = []

	for word in words:
		word_found = False
		for item in histogram:
			if word == item[0]:
				item[1] += 1
				word_found = True
				break
		if not word_found:
			histogram.append([word, 1])

	return histogram


def histogram_list_of_tuples(words):
	'''returns a list of tuples with the type and token'''
	# TUPLE APPROACH O(n^2)

	tuple_histogram = []
	
	for word in words:
		found = False
		for item in tuple_histogram:
			if word == item[0]:
				count = item[1] + 1
				tuple_histogram.remove(item)
				tuple_histogram.append((word, count))
				found = True
				break
		if not found:
			tuple_histogram.append((word, 1))

	return tuple_histogram


def list_of_counts(dictionary):
	'''returns a list of of tuples where the item at [0] is the tokens and item at [1] is a list of types which have that amount of tokens'''
	# implement a dictionary. loop through dictionary, add the dict[1] item to the first index in the new_tuple_list
	# as (dict[1], [dict[0]]). if dict[1] is in new_tuple_list, append the dict[0] in the tuple value

	# dictionary = {'one': 1, 'blue': 1, 'two': 1, 'fish': 4, 'red': 1}

	new_tuple_list = []


	for key, value in dictionary.items():
		found = False
		for item in new_tuple_list:
			if value == item[0]:
				found = True
				array = item[1]
				array.append(key)
				new_tuple_list.remove(item)
				new_tuple_list.append((value, array))
				break
		if not found:
			new_tuple_list.append((value, [key]))

	return new_tuple_list


def unique_words(list_counts):
	'''return the amount of unique words in the file and return the words'''
	unique_count = 0
	for item in list_counts:
		if item[0] == 1:
			counts_of_one = len(item[1])
			return (counts_of_one)
			break


def frequency(word, histogram):
	return histogram[word]


def most_frequent_count(histogram):
	# use the reduce function to compare all values of the histogram and return the key/keys with the largest values.
	current_largest = 1
	most_frequent_word = ""
	for key, value in histogram.items():
		if value >= current_largest:
			current_largest = value
			most_frequent_word = key

	return ("Most frequent word: \"" + most_frequent_word + "\", "+ str(current_largest) + " times")



if __name__ == "__main__":

	word_array = file_to_word_array('BreakfastAtTiffanys.txt')
	# print(word_array)
	dictio = histogram_dict(word_array)
	# print(dictio)
	# print(histogram_list_of_lists(word_array))
	# print(histogram_list_of_tuples(word_array))
	# print(list_of_counts(dict))
	# print("frequency of word the word \"love\": ", frequency('love', dictio))
	# print("unique word count: ", unique_words(list_of_counts(dictio)))
	# print(most_frequent_count(dictio))
