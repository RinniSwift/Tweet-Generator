import random

def sample_word():

	word_array = "one fish two fish green fish blue fish".split()

	histogramm = {}
	for word in word_array:
		if word in histogramm.keys():
			histogramm[word] += 1
		else:
			histogramm[word] = 1

	count = 0
	new_histogram = {}
	for key, value in histogramm.items():
		posibil = (value / len(word_array))
		new_histogram[key] = [count]
		count += posibil
		new_histogram[key].append(count)


	random_number = random.random()
	print(random_number)
	# answer = ""
	for key, value in new_histogram.items():
		if value[0] < random_number < value[1]:
			return key

	# if answer == "":
	# 	return 0
	# else:
	# 	return answer



	



	# print("histogramm: ", histogramm)
	# print("histogram_probability: ", histogram_probability)
	# print("possibilities: ", possibilities)
	

if __name__ == "__main__":
	print(sample_word())