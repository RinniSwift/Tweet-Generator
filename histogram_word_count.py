
def histogram(file):

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

	return most_frequent_word, current_largest


if __name__ == "__main__":
	print(histogram('BreakfastAtTiffanys.txt'))
	print("frequency of word: ", frequency('love', histogram('BreakfastAtTiffanys.txt')))
	print("unique words: ", unique_words(histogram('BreakfastAtTiffanys.txt')))
	print(most_frequent_count(histogram('BreakfastAtTiffanys.txt')))



# create a class called histogram and put the functions in
