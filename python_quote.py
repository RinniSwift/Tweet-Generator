import random
import sys

quotes = ("It's just a flesh wound.", 
		  "He's not the Messiah. He's a very naughty boy!",
          "THIS IS AN EX-PARROT!!")

def random_python_quote():
	rand_ind = random.randint(0, len(quotes) - 1)
	return quotes[rand_ind]


def rearange_input():
	# append all users input items into a list

	array = sys.argv[1:]

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



def list_to_string(list):
	string = " "
	return string.join(list)



if __name__ == '__main__':
	quote = random_python_quote()
	print(quote)
	rearange = rearange_input()
	join_string = list_to_string(rearange)
	print(join_string)
