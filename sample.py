import random

def sample_word():

	word_array = "one fish two fish green fish blue fish".split()

	# create a dictionary which will store the word as the key and the frequency as the value
	histogramm = {}
	for word in word_array:
		if word in histogramm.keys():
			histogramm[word] += 1
		else:
			histogramm[word] = 1

	# create a dictionary which will store the word as the key and the possibility it will occur in as an array as the value
	# e.g. {'one': [0, 0.125], 'fish': [0.125, 0.625], ...}
	count = 0
	new_histogram = {}
	for key, value in histogramm.items():
		posibil = (value / len(word_array))
		new_histogram[key] = [count]
		count += posibil
		new_histogram[key].append(count)

	# random a number from 0...1
	random_number = random.random()
	# print(random_number)
	# check if the random number is between the value[0] and value[1] of the dictionary
	# if is, the possibility has fallen into that word, return the word
	for key, value in new_histogram.items():
		if value[0] < random_number < value[1]:
			return key

	# print("histogramm: ", histogramm)
	# print("histogram_probability: ", histogram_probability)
	# print("possibilities: ", possibilities)

def test_sample_word():

	histogram = {}

	for i in range(0, 1000):
		sample = sample_word()
		# append the word count found by one or add to the word count found
		if sample in histogram:
			histogram[sample] += 1
		else:
			histogram[sample] = 1

	return histogram

	

if __name__ == "__main__":
	print(sample_word())
	print(test_sample_word())



