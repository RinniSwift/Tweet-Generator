
def file_to_word_array(file):

	with open(file, 'r') as f:
		text_content = f.read()
	words = text_content.lower().strip("(),!.?""/").split()
	return words


def histogram_dict(file):

	# DICTIONARY APPROACH O(n)

	histogram = {}

	with open(file, 'r') as f:
		text_content = f.read()

	words = text_content.lower().strip("(),!.?""/").split()

	# loop through all words in the text file and check if the word contains in the histogram, make the count 1, or else add 1 to the previous count
	for word in words:
		if word in histogram.keys():
			histogram[word] += 1
		else:
			histogram[word] = 1

	# return a histogram with the count of word frequency
	return histogram

def histogram_list_of_lists(file):

	# LIST APPROACH O(n^2)

	histogram = []

	with open(file, 'r') as f:
		file_content = f.read()
	words = file_content.split()

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


def histogram_list_of_tuples(list_):

	# TUPLE APPROACH O(n^2)

	tuple_histogram = []

	
	for word in list_:
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


def unique_words(histogram):
	unique_count = 0
	for key, value in histogram.items():
		if value == 1:
			unique_count += 1
	return unique_count


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

def list_of_counts():
	#implement the dictionary and reverse to list of counts
	pass


if __name__ == "__main__":

	word_array = file_to_word_array('BreakfastAtTiffanys.txt')
	# print(histogram_dict('BreakfastAtTiffanys.txt'))
	# print("frequency of word the word \"love\": ", frequency('love', histogram('BreakfastAtTiffanys.txt')))
	# print("unique word count: ", unique_words(histogram('BreakfastAtTiffanys.txt')))
	# print(most_frequent_count(histogram('BreakfastAtTiffanys.txt')))
	# print(histogram_list_of_lists('BreakfastAtTiffanys.txt'))
	print(histogram_list_of_tuples(word_array))



# create a class called histogram and put the functions in
