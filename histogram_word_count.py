
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
	print("something")

def frequency(word):
	print("something")


if __name__ == "__main__":
	print(histogram('BreakfastAtTiffanys.txt'))