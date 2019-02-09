import random
import sys



def random_python_quote():

	quotes = ("It's just a flesh wound.", 
		  "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

	rand_ind = random.randint(0, len(quotes) - 1)
	return quotes[rand_ind]


def rearange_input():
	# append all users input items into a list

	array = sys.argv[1:]

	'''
	return random.sample(array, len(array))
	'''

	'''
	result_array = []
	for i in range(1, len(sys.argv)):
		item = random.choice(array)
		result_array.append(item)
		array.remove(item)
	return result_array
	'''

	for i in range(len(array)):
		rand_int = random.randint(0, len(array) - 1)
		array[rand_int], array[i] = array[i], array[rand_int]

	return array



def reverse_words():
	array = sys.argv[0:]
	new_array = []

	for i in range(len(array) - 1, 0, -1):
		new_array.append(array[i])

	return new_array


def list_to_sentence(list):
	'''returns sentence from an array of words'''
	return " ".join(list) 



if __name__ == '__main__':
	quote = random_python_quote()
	# print(quote)
	rearange_arr = rearange_input()
	join_string = list_to_sentence(rearange_arr)
	# print(join_string)
	
	reverse_word_order = reverse_words()
	print(list_to_sentence(reverse_word_order))
