
def histogram(file):

	# *** how to remove ',.' at the end of words ***
	# DICTIONARY APPROACH

	histogram = {}

	with open(file, 'r') as f:
		text_content = f.read()
	words = text_content.split()

	# loop through all words in the text file and check if the word contains in the histogram, make the count 1, or else add 1 to the previous count
	for word in words:
		if word in histogram.keys():
			histogram[word] += 1
		else:
			histogram[word] = 1

	# return a histogram with the count of word frequency
	return histogram

def histogram_list_of_lists(file):

	histogram = []

	with open(file, 'r') as f:
		file_content = f.read()
	words = file_content.split()

	# loop through indexes of the word file
	for i in range(len(words)):
		word_found = False
		# if histogram is not empty
		if histogram:
			# loop through the indexes of the histogram
			for j in range(len(histogram)):
				# if the word contains in the histogram
				if histogram[j][0] == words[i]:
					# add the count by one
					histogram[j][1] += 1
					word_found = True
					break 

			if not word_found:
				histogram.append([words[i], 1])

		# if histogram is empty
		else:
			histogram.append([words[i], 1])

	return histogram


def histogram_list_of_tuples(list_of_lists):
	return tuple(list_of_lists)






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



if __name__ == "__main__":
	# histogram('BreakfastAtTiffanys.txt')
	# print("frequency of word the word \"love\": ", frequency('love', histogram('BreakfastAtTiffanys.txt')))
	# print("unique word count: ", unique_words(histogram('BreakfastAtTiffanys.txt')))
	# print(most_frequent_count(histogram('BreakfastAtTiffanys.txt')))
	# print(histogram_list_of_lists('BreakfastAtTiffanys.txt'))
	print(histogram_list_of_tuples(histogram_list_of_lists('BreakfastAtTiffanys.txt')))



# create a class called histogram and put the functions in
